class RepeatCellUpdate:

    def __init__(self, range, cell_data, fields, **kwargs):
        self.range = range
        self.cell = {}
        self.fields = fields
        self._construct_cell_data()
    
    def _construct_cell_data(self):
        self._field_mask_string_to_dict(self.fields)

    def _field_mask_string_to_dict(self, field_mask_string):
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