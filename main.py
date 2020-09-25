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

# def key_pressed(mode: Mode, key: Key):
    
#     print(f"START: mode: {mode.name}, Key: {key}")
#     time.sleep(2)
#     print(f"END: mode: {mode.name}, Key: {key}")

keypad = Keypad(Mode)


keypad.start()

#keypad.start(key_pressed)