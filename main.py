from keypad import Keypad, Key
import time

from enum import IntEnum

# Using enum class create enumerations
class Mode(IntEnum):
    Teams = 0
    Sonos = 1
    Another = 2


keypad = Keypad(Mode)

def key_pressed(mode: Mode, key: Key):
    print(f"START: mode: {mode}, Key: {key}")
    time.sleep(2)
    print(f"END: mode: {mode}, Key: {key}")


keypad.start(key_pressed)

