from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os.path

class GoogleAPIClient:
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    def __init__(self):
        creds = self._get_credentials()
        self._service = self._build_service(creds)

    def _get_credentials(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is created
        # automatically when the authorization flow completes for the first time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except:
                    os.remove("token.json")
                finally:
                    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                    creds = flow.run_local_server(port=0)
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds
    
    def _build_service(self, creds):
        try:
            service = build('sheets', 'v4', credentials=creds)
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error
        return service

    def batch_update(self, spreadsheet):
        # spreadsheet._clean_up_requests()
        self._service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet.spreadsheet_id, body=spreadsheet.to_dict()).execute()
        spreadsheet.reset_updates()
    
    