def color(red=0, green=0, blue=0):
    return Color(red, green, blue)


class Color(object):
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def to_hex(self):
        return '#%02x%02x%02x' % (int(self.red), int(self.green), int(self.blue))
