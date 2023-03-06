#TODO Turn into 2 classes: SpreadsheetValues and SpreadsheetFormat

from updates.repeat_cell_update import RepeatCellUpdate

class Spreadsheet:

    def __init__(self, spreadsheet_id):
        self._updates = []
        self.spreadsheet_id = spreadsheet_id

    def reset_updates(self):
        self._updates = []
        print("Resetting...")

    def to_dict(self):
        return {'requests' : self._updates}
    
    # def _clean_up_text_formats(self):
    #     for update in self._updates:
    #         if (update.get('repeatCell') is not None):
    #             print(update['repeatCell']['cell'])

    def vertical_alignment(self, range, alignment):
        if alignment not in ["TOP", "MIDDLE", "BOTTOM"]:
            raise ValueError
        self._updates.append(RepeatCellUpdate(range, verticalAlignment = alignment).to_request_dict())
        # print(self._updates)

    def horizontal_alignment(self, range, alignment):
        if alignment not in ["LEFT", "CENTER", "RIGHT"]:
            raise ValueError
        self._updates.append(RepeatCellUpdate(range, horizontalAlignment = alignment).to_request_dict())
        # print(self._updates)
    
    def wrap_strategy(self, range, strategy):
        if strategy not in ["OVERFLOW_CELL", "CLIP", "WRAP"]:
            raise ValueError
        self._updates.append(RepeatCellUpdate(range, wrapStrategy = strategy).to_request_dict())
        # print(self._updates)
    
    def bold(self, range):
        self._updates.append(RepeatCellUpdate(range, bold = True).to_request_dict())
        # print(self._updates)
    
    def italic(self, range):
        self._updates.append(RepeatCellUpdate(range, italic = True).to_request_dict())
        # print(self._updates)
    
    def strikethrough(self, range):
        self._updates.append(RepeatCellUpdate(range, strikethrough = True).to_request_dict())
        # print(self._updates)
    
    def underline(self, range):
        self._updates.append(RepeatCellUpdate(range, underline = True).to_request_dict())
        # print(self._updates)
    
    def background_color_style(self, range, color):
        self._updates.append(RepeatCellUpdate(range, backgroundColorStyle = color).to_request_dict())
        # print(self._updates)

    def foreground_color_style(self, range, color):
        self._updates.append(RepeatCellUpdate(range, foregroundColorStyle = color).to_request_dict())
        # print(self._updates)