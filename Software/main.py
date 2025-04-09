import board
import digitalio 
from kb import KMKKeyboard, isRight
from storage import getmount
from kmk.keys import KC, Key
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.hid import HIDModes

import supervisor

WIRED = supervisor.runtime.usb_connected
keyboard = KMKKeyboard()

keyboard.tap_time = 100

layers = Layers()


split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT

print('Right' if isRight else 'Left')

split = Split(
    split_type=SplitType.BLE,
    split_side=split_side,
)

keyboard.modules = [layers, split]

LOWER =KC.MO(1)
RAISE =KC.MO(2)

keyboard.keymap = [

    [  #QWERTY
                                            KC.RALT,			             KC.TAB,\

        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,      KC.U,    KC.I,    KC.O, KC.P,\

        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,      KC.J,    KC.K,    KC.L, KC.BSPC,\

        KC.Z,    KC.X,    KC.C,    KC.V,    KC.COMM,                     KC.DOT,    KC.N,    KC.M,    KC.B, KC.ESC,\
                                            
                          KC.NO, 				                                             KC.NO,\

                          KC.LSHIFT,   LOWER, KC.SPACE,              		 KC.ENT, RAISE,   KC.LCTRL,
                                                    

    ],

    [  #LOWER	
                                           					                           KC.NO, 			                KC.NO,\

        KC.N1,          KC.N2,           KC.N3,           	     KC.N4,                KC.N5,                           KC.N6,      KC.N7,     KC.N8,     KC.N9,    KC.N0,\

        KC.LCTL(KC.A),  KC.LCTL(KC.S),   KC.LCTL(KC.RALT(KC.T)), KC.QUES,              KC.LCTL(KC.V),                   KC.N0,      KC.LEFT,   KC.DOWN,   KC.UP,    KC.RIGHT,\

        KC.LCTL(KC.Z),  KC.LCTL(KC.X),   KC.LCTL(KC.INSERT),     KC.LSFT(KC.INSERT),   KC.LCTL(KC.C),                   KC.GRAVE,   KC.LABK,   KC.PIPE,   KC.RABK,  KC.SLSH,\
                                                                                       
                                         KC.BT_NXT, 				                                                                               KC.BT_PRV,\
 
                                         KC.LSHIFT,                  KC.NO,                KC.SPACE,                        KC.ENT,     KC.NO,     KC.LCTRL,
    ],

    [  #RAISE
                                              KC.NO,			    KC.NO,\

        KC.EXLM,   KC.AT, KC.HASH,  KC.DLR,   KC.PERC,                      KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,\

        KC.F2,     KC.F5,   KC.F9,  KC.QUOT,  KC.SCLN,                      KC.UNDS,  KC.EQL, KC.LCBR, KC.RCBR, KC.DEL,\

        KC.F12,    KC.F11,  KC.F10, KC.DQUO,  KC.COLON,                     KC.MINS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS,\

                            KC.NO, 				                                              KC.NO,\

                          KC.LSHIFT,   KC.NO,   KC.SPACE,                       KC.ENT,      KC.NO,    KC.LCTRL,
    ]

]


if __name__ == '__main__':
    if isRight or WIRED:
        keyboard.go()
    else:
        keyboard.go(hid_type=HIDModes.BLE, ble_name='Keeb')

