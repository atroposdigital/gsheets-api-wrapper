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
    
    def vertical_alignment(self, range, alignment):
        if alignment not in ["TOP", "MIDDLE", "BOTTOM"]:
            raise ValueError
        self._updates.append(RepeatCellUpdate(range, verticalAlignment = alignment).to_request_dict())
        print(self._updates)

    def horizontal_alignment(self, range, alignment):
        if alignment not in ["LEFT", "CENTER", "RIGHT"]:
            raise ValueError
        self._updates.append(RepeatCellUpdate(range, horizontalAlignment = alignment).to_request_dict())
        print(self._updates)
    
    def bold(self, range):
        self._updates.append(RepeatCellUpdate(range, bold = True).to_request_dict())
        print(self._updates)
    
    def background_color(self, range, color):
        self._updates.append(RepeatCellUpdate(range, backgroundColor = color).to_request_dict())
        print(self._updates)