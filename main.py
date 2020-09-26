from keypad import Keypad, Key
import time

from enum import IntEnum


class Mode(IntEnum):
    AMode = 0
    OneMore = 1
    Another = 2
    AndAnother = 3
    YetAnother = 4
    HowMany =5
    MaybeOne = 6
    OkLastOne =7

keypad = Keypad(Mode)


def key_pressed(mode: Mode, key: Key):
    print(f"START: mode: {mode.name}, Key: {key}")
    time.sleep(2)
    print(f"END: mode: {mode.name}, Key: {key}")


actions = {

    Mode.AMode: { 
        Key.KEY1: lambda: print("M1K1"),
        Key.KEY2: lambda: print("M1K2")
    },
    Mode.OneMore: {
        Key.KEY1: lambda: print("M2K1"),
        Key.KEY3: lambda: print("M2K3")
    },
    Mode.Another: {
        Key.KEY2: lambda: print("M3K2"),
        Key.KEY3: lambda: print("M3K3"),
        Key.KEY4: lambda: print("M3K4"),
        Key.ROT_BUT: lambda: print("M3KRB"),
        Key.ROT_CCW: lambda: print("M3KRCCW")
    }
}


#keypad.start(key_pressed)
keypad.start(actions)