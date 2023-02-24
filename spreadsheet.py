from updates.repeat_cell_update import RepeatCellUpdate

class Spreadsheet:

    def __init__(self, spreadsheet_id):
        self._updates = []
        self.spreadsheet_id = spreadsheet_id

    def reset_updates(self):
        self._updates = []

    def to_dict(self):
        return {'requests' : self._updates}
    
    def vertical_alignment_all(self, sheet_id, alignment):
        if alignment not in ["TOP", "MIDDLE", "BOTTOM"]:
            raise ValueError
        update = RepeatCellUpdate(sheet_id,"asda","automaticFormat(horizontalAlignment,cellFormat,textFormat),dataValidation,customFormat(verticalAlignment,sheetColoring),userEnteredFormat.textFormat.foregroundColorStyle", userEnteredFormat_value = alignment)