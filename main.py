from google_api_client import GoogleAPIClient
from spreadsheet import Spreadsheet
from util.range import Range
from util.color import Color

client = GoogleAPIClient()

ss = Spreadsheet("1JkU69mcn8YdqV2Pvflo65iNwS7i3BuOAySOWExlcg84")

range = Range(sheet_id = 0, full_sheet = True)
ss.vertical_alignment(range, "MIDDLE")

range = Range(sheet_id = 0, no_of_columns=5)
ss.horizontal_alignment(range, "CENTER")

range = Range(sheet_id = 0, no_of_rows=1)
ss.bold(range)

range = Range(sheet_id = 0 , no_of_rows=1, no_of_columns=5)
ss.background_color(range,Color("f6b26b"))

client.batch_update(ss)

print(ss._updates)