from google_api_client import GoogleAPIClient
from spreadsheet import Spreadsheet
from models.range import Range
from models.color import Color

client = GoogleAPIClient()

ss = Spreadsheet("1JkU69mcn8YdqV2Pvflo65iNwS7i3BuOAySOWExlcg84")

range = Range(sheet_id = 0)
ss.vertical_alignment(range, "MIDDLE")

range = Range(sheet_id = 0, last_column = 4)
ss.horizontal_alignment(range, "CENTER")

range = Range(sheet_id = 0, last_row = 1)
ss.bold(range)

range = Range(sheet_id = 0, last_row = 0, last_column = 4)
ss.background_color(range,Color("f6b26b"))

client.batch_update(ss)

print(ss._updates)
#Color(hex = "f6b26b")