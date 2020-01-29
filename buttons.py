
def get_bit(value, n):
    return (value >> n & 1) != 0


def flip_bit(value, n):
    return value ^ (1 << n)


class Buttons:
    """
    Utility class to set buttons in the input report
    https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering/blob/master/bluetooth_hid_notes.md
    Byte 	0 	    1 	    2 	    3 	    4 	    5 	    6 	    7
    1   	Y 	    X 	    B 	    A 	    SR 	    SL 	    R 	    ZR
    2       Minus 	Plus 	R Stick L Stick Home 	Capture
    3       Down 	Up 	    Right 	Left 	SR 	    SL 	    L 	    ZL
    """
    def __init__(self):
        # 3 bytes
        self.byte_1 = 0
        self.byte_2 = 0
        self.byte_3 = 0

        # generating methods for each button
        def gen_methods(byte, bit):
            def flip():
                setattr(self, byte, flip_bit(getattr(self, byte), bit))

            def getter():
                return get_bit(getattr(self, byte), bit)
            return flip, getter

        # byte 1
        self.y, self.y_is_set = gen_methods('byte_1', 0)
        self.x, self.x_is_set = gen_methods('byte_1', 1)
        self.b, self.b_is_set = gen_methods('byte_1', 2)
        self.a, self.a_is_set = gen_methods('byte_1', 3)
        self.right_sr, self.right_sr_is_set = gen_methods('byte_1', 4)
        self.right_sl, self.right_sl_is_set = gen_methods('byte_1', 5)
        self.r, self.r_is_set = gen_methods('byte_1', 6)
        self.zr, self.zr_is_set = gen_methods('byte_1', 7)

        # byte 2
        self.minus, self.minus_is_set = gen_methods('byte_2', 0)
        self.plus, self.plus_is_set = gen_methods('byte_2', 1)
        self.r_stick, self.r_stick_is_set = gen_methods('byte_2', 2)
        self.l_stick, self.l_stick_is_set = gen_methods('byte_2', 3)
        self.home, self.home_is_set = gen_methods('byte_2', 4)
        self.capture, self.capture_is_set = gen_methods('byte_2', 5)

        # byte 3
        self.down, self.down_is_set = gen_methods('byte_3', 0)
        self.up, self.up_is_set = gen_methods('byte_3', 1)
        self.right, self.right_is_set = gen_methods('byte_3', 2)
        self.left, self.left_is_set = gen_methods('byte_3', 3)
        self.left_sr, self.left_sr_is_set = gen_methods('byte_3', 4)
        self.left_sl, self.left_sl_is_set = gen_methods('byte_3', 5)
        self.l, self.l_is_set = gen_methods('byte_3', 6)
        self.zl, self.zl_is_set = gen_methods('byte_3', 7)

    """
    Example for generated methods: home button (byte_2, 4)

    def home(self):
        self.byte_2 = flip_bit(self.byte_2, 4)

    def home_is_set(self):
        return get_bit(self.byte_2, 4)
    """

    def to_list(self):
        return [self.byte_1, self.byte_2, self.byte_3]

    def clear(self):
        self.byte_1 = self.byte_2 = self.byte_3 = 0
