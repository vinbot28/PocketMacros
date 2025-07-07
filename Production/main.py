# Code written using ChatGPT
print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import RotaryEncoder
from kmk.modules.oled import OLED
from kmk.oled.basic import BasicDisplay
from adafruit_ssd1306 import SSD1306_I2C

from kmk.layers import Layers

# ----------------------------
# Keyboard setup
# ----------------------------
keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP0, board.GP3, board.GP4)
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ----------------------------
# Layers extension
# ----------------------------
layers_ext = Layers()
keyboard.extensions.append(layers_ext)

# ----------------------------
# Keymap with Layer Toggle
# ----------------------------
keyboard.keymap = [
    # Layer 0
    [KC.KP_7, KC.KP_8, KC.KP_9, KC.ESC],     # row 0
    [KC.KP_4, KC.KP_5, KC.KP_6, KC.TG(1)],   # row 1
    [KC.KP_1, KC.KP_2, KC.KP_3, KC.ENT],     # row 2

    # Layer 1
    [KC.F1, KC.F2, KC.F3, KC.TRNS],
    [KC.F4, KC.F5, KC.F6, KC.TRNS],
    [KC.F7, KC.F8, KC.F9, KC.TRNS],
]

# ----------------------------
# Rotary Encoder for Volume
# ----------------------------
encoder = RotaryEncoder(
    pin_num_clk=board.GP2,
    pin_num_dt=board.GP1,
    pin_num_sw=None, 
)

def encoder_turn(pressed, clockwise):
    if clockwise:
        keyboard.tap_code(KC.VOLU)
    else:
        keyboard.tap_code(KC.VOLD)

encoder.rotate = encoder_turn
keyboard.modules.append(encoder)

# ----------------------------
# OLED Setup: 128x32, I2C on GP6/GP7
# ----------------------------
i2c = board.I2C()
display_driver = SSD1306_I2C(128, 32, i2c)
oled = OLED(display_driver, BasicDisplay)
keyboard.modules.append(oled)

# OLED display current layer
def oled_task():
    oled.display.clear()
    oled.display.draw_text(0, 0, "Layer:")
    oled.display.draw_text(0, 12, str(keyboard.current_layer))
    oled.display.show()

oled.task = oled_task

# ----------------------------
# Run it
# ----------------------------
if __name__ == '__main__':
    keyboard.go()
