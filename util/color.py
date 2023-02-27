class Color:

    def __init__(
        self,
        hex,       
    ):
        
        self.rgb = self._hex_to_rgb(hex)
        self.rgb = self._rgb_to_canonicalized_rgb(self.rgb)

        print(self.to_dict())

    def _hex_to_rgb(self, hex):
        return [int(hex[i:i+2], 16)  for i in (0, 2, 4)]
    
    def _rgb_to_canonicalized_rgb(self, rgb):
        return [color/255 for color in rgb] 
    
    def to_dict(self):
        return {"red": self.rgb[0], "green": self.rgb[1], "blue": self.rgb[2]}