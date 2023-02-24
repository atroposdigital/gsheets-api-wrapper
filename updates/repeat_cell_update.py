class RepeatCellUpdate:

    def __init__(self, range, cell_data, fields, **kwargs):
        self.range = range
        self.cell = {}
        self.fields = fields
        self._construct_cell_data()
    
    def _construct_cell_data(self):
        self._field_mask_string_to_json(self.fields)

    def _field_mask_string_to_json(self, field_mask_string):
        field_mask_json = {}
        current = field_mask_json

        parts = field_mask_string.split(".")

        for i in range(len(parts)):
            part = parts[i]
            if "(" in part:
                parts[i] = part.split('(')
            

        print (parts)

        # for i in range(len(parts)):
        #     part = parts[i]
        #     #next_part = parts[i+1]
        #     if "(" in parts[i]:
        #         key, value = part.split('(')
        #         current[key] = {}
        #         current = current[key]
        #         value = value.split(')')[0].split(',')
        #         for subpart in value:
        #             current[subpart] = None
                
        #         print(field_mask_json)
        #         print(value)

        # print(parts)
        # print("\n")

        # for part in parts:
        #     if '(' in part:
        #         key, value = part.split('(')
        #         current[key] = {}
        #         current = current[key]
        #         subparts = value.rstrip(')').split(',')
        #         for subpart in subparts:
        #             current[subpart] = None
        #     else:
        #         current[part] = {}
        #         current = current[part]

        # print(field_mask_json)