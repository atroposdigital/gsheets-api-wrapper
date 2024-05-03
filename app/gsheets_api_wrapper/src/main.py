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
ss.italic(range)

range = Range(sheet_id = 0, last_row = 0, last_column = 4)
ss.background_color_style(range,Color("f6b26b"))

range = Range(sheet_id = 0, first_row = 2, last_row = 3, first_column = 4, last_column = 5)
ss.wrap_strategy(range, "WRAP")

range = Range(sheet_id = 0, last_row = 0)
ss.bold(range)
ss.foreground_color_style(range, Color("ffffff"))


client.batch_update(ss)

# print(ss._updates)
#Color(hex = "f6b26b")