from google_api_client import GoogleAPIClient
from spreadsheet import Spreadsheet

client = GoogleAPIClient()

ss = Spreadsheet("1JkU69mcn8YdqV2Pvflo65iNwS7i3BuOAySOWExlcg84")

ss.vertical_alignment_all(1, "MIDDLE")