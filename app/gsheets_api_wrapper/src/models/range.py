#TODO define a Range class that can be instansiated in both A1 notation and GridRange notation, that also has helper functions to output what you need

class Range:

    def __init__(
        self,
        sheet_id,
        first_row = None,
        last_row = None,
        first_column = None,
        last_column = None,
    ):
        
        self.sheet_id = sheet_id
    
        self._startRowIndex = first_row
        self._endRowIndex = last_row + 1 if last_row is not None else None

        self._startColumnIndex = first_column
        self._endColumnIndex = last_column + 1 if last_column is not None else None

        self.final_range = self._for_custom_range()

        print(self.get())
    
    def get(self):
        return self.final_range

    def _for_custom_range(self):
        range_object = {'sheetId': self.sheet_id}
        if self._startRowIndex is not None:
            range_object['startRowIndex'] = self._startRowIndex
        if self._endRowIndex is not None:
            range_object['endRowIndex'] = self._endRowIndex
        if self._startColumnIndex is not None:
            range_object['startColumnIndex'] = self._startColumnIndex
        if self._endColumnIndex is not None:
            range_object['endColumnIndex'] = self._endColumnIndex
        return range_object
    

#TODO set up these as tests

# Range(0, first_row=1, last_row=1, first_column=1, last_column=1)
# Range(0, full_sheet=True)
# Range(0, first_row=3, last_row=4, first_column=1, last_column=2)
# Range(0, first_column=1, last_column=2)

# {'sheetId': 0, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 1}
# {'sheetId': 0}
# {'sheetId': 0, 'startRowIndex': 2, 'endRowIndex': 4, 'startColumnIndex': 0, 'endColumnIndex': 2}
# {'sheetId': 0, 'startColumnIndex': 0, 'endColumnIndex': 2}