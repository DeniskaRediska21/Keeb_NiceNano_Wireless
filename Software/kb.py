import board
import digitalio

from storage import getmount

import kmk
from kmk import kmk_keyboard
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder

name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

# GPIO to key mapping, Left
_KEY_CFG_LEFT = [
board.P0_31,
board.P0_02,board.P0_10,board.P0_09,board.P1_06,board.P1_04,
board.P0_29,board.P1_11,board.P0_24,board.P1_02,board.P0_11,
board.P0_22,board.P1_13,board.P1_07,board.P1_00,board.P0_20,
board.P1_01,
board.P0_08,board.P0_06,board.P0_17,
]

# GPIO to key mapping, Right
_KEY_CFG_RIGHT = [
board.P1_01,
board.P1_13,board.P1_02,board.P1_04,board.P0_24,board.P0_17,
board.P1_11,board.P0_09,board.P0_11,board.P0_22,board.P0_08,
board.P1_15,board.P0_10,board.P1_00,board.P0_20,board.P0_06,
board.P1_07,
board.P0_31,board.P0_29,board.P0_02,
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            pins=_KEY_CFG_RIGHT if isRight else _KEY_CFG_LEFT,
            value_when_pressed=False,
            pull=True,
            interval=0.02,
            max_events=64
        )

    coord_mapping = [
                         0,   20,
         1,  2,  3,  4,  5,   21, 22, 23, 24, 25,
         6,  7,  8,  9, 10,   26, 27, 28, 29, 30,
        11, 12, 13, 14, 15,   31, 32, 33, 34, 35,
                16,                   36,
                17, 18, 19,   37, 38, 39
    ]

