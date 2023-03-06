class RepeatCellUpdate:

    def __init__(
        self,
        range,
        verticalAlignment = None,
        horizontalAlignment = None,
        bold = False,
        italic = False,
        backgroundColor = None,
        wrapStrategy = None,
    ):
        
        self._range = range.get()

        self._cell_data = {}
        self._fields = []

        if verticalAlignment is not None:
            self._add_to_cell_data({'verticalAlignment': verticalAlignment})
            self._fields.append('userEnteredFormat.verticalAlignment')

        if horizontalAlignment is not None:
            self._add_to_cell_data({'horizontalAlignment': horizontalAlignment})
            self._fields.append('userEnteredFormat.horizontalAlignment')

        if bold:
            self._add_to_cell_data({'textFormat': {'bold': True}})
            self._fields.append('userEnteredFormat.textFormat')

        if italic:
            self._add_to_cell_data({'textFormat': {'italic': True}})
            self._fields.append('userEnteredFormat.textFormat')    

        #TODO update to backgroundColorStyle
        if backgroundColor is not None:
            self._add_to_cell_data({'backgroundColor': backgroundColor.get()})
            self._fields.append('userEnteredFormat.backgroundColor')

        if wrapStrategy is not None:
            self._add_to_cell_data({'wrapStrategy': wrapStrategy})
            self._fields.append('userEnteredFormat.wrapStrategy')
    
    def _add_to_cell_data(
        self,
        value,
        key = "userEnteredFormat"
    ):
        if self._cell_data.get(key) is None:
            self._cell_data[key] = value
        else:
            self._cell_data[key].update(value)

    def to_request_dict(self):
        return {
            'repeatCell': {
                'range': self._range,
                'cell': self._cell_data,
                'fields': ",".join(self._fields)
            }
        }

    def _field_mask_string_to_dict(self, field_mask_string):
        # Use this for test:
        #update = RepeatCellUpdate(sheet_id,"asda","automaticFormat(horizontalAlignment,cellFormat,textFormat),  \
        # dataValidation,customFormat(verticalAlignment,sheetColoring),userEnteredFormat.textFormat.foregroundColorStyle", userEnteredFormat_value = alignment)
        def _separate_transitive(parts):
            reconstruct = []
            reconstruct_flag = False
            reconstruct_index = 0
            for i in range(len(parts) - 1, -1, -1):
                part = parts[i]

                if ")" in part:
                    reconstruct_flag = True
                    reconstruct.append([])

                if reconstruct_flag:
                    reconstruct[reconstruct_index].insert(0, part.replace(")",""))
                    parts.pop(i)

                if "(" in part:
                    reconstruct_flag = False
                    reconstruct_index += 1
            return parts, reconstruct

        def _flatten_reconstruct_list(reconstruct):
            for i in range(len(reconstruct)): 
                reconstruct[i] = reconstruct[i][0].split("(") + reconstruct[i][1:]
            return reconstruct
        
        def _apply_transitive(parts, reconstruct):
            for i in range(len(reconstruct)):
                key = reconstruct[i][0]
                for y in range(1, len(reconstruct[i])):
                    parts.append(key + "." + reconstruct[i][y])
            return parts

        def _add_parts_to_dict(parts):
            field_mask_dict = {}

            for i in range(len(parts)):
                current = field_mask_dict
                subparts = parts[i].split('.')
                for y in range(len(subparts)):
                    key = subparts[y]
                    if key not in field_mask_dict.keys():
                        current[key] = {}
                    if y == len(subparts) - 1:
                        current[key] = None
                    current = current[key]

            return field_mask_dict
        
        print(field_mask_string)

        parts = field_mask_string.split(",")
        parts, reconstruct = _separate_transitive(parts)
        reconstruct = _flatten_reconstruct_list(reconstruct)
        parts = _apply_transitive(parts, reconstruct)
        self.cell = _add_parts_to_dict(parts)

        print(self.cell)