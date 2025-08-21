import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (board.TX, board.MOSI, board.MISO)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[
    KC.KP_7, KC.KP_8, KC.KP_9, KC.ESC,
    KC.KP_4, KC.KP_5, KC.KP_6, KC.NO,
    KC.KP_1, KC.KP_2, KC.KP_3, KC.ENT
]]

keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()



