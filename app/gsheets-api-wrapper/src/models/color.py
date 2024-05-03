class Color:

    _increments = {"red": 0, "green": 2, "blue": 4}

    def __init__(
        self,
        hex = None,
        rgb = None,       
    ):
        
        if hex is not None:
            self.rgb = self._hex_to_rgb(hex)
        elif rgb is not None:
            self.rgb = rgb
        else:
            raise ValueError
        
        self.rgb = self._rgb_to_canonicalized_rgb(self.rgb)

        print(self.get())

    def _hex_to_rgb(self, hex):
        return {color: int(hex[i:i+2], 16) for color, i in self._increments.items()}

    def _rgb_to_canonicalized_rgb(self, rgb):
        return {color: i/255 for color, i in rgb.items()}
    
    def get(self):
        return self.rgb