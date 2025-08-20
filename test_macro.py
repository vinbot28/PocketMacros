import board

from kmk.kmk_keyboard import kmk_keyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26,)
keyboard.row_pins = (board.GP0,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.KP_5,]
]
if __name__ == '__main__':
    keyboard.go()
