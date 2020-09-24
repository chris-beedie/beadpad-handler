from keypad import Keypad, Key
import time

from enum import IntEnum


class Mode(IntEnum):
    Teams = 0
    Sonos = 1
    Another = 2

keypad = Keypad(Mode)


actions = {

    Mode.Teams: { 
        Key.KEY1: lambda: print("TK1"),
        Key.KEY2: lambda: print("TK2")
    },
    Mode.Sonos: {
        Key.KEY1: lambda: print("SK1"),
        Key.KEY3: lambda: print("TK3")
    }
}

def key_pressed(mode: Mode, key: Key):
    
    print("user defined")
    action = (
        actions
        .get(mode,{})
        .get(key,lambda: print(f"no action defined for '{key.name}' in mode '{mode.name}'"))
    )
    
    action()



#keypad.start(key_pressed)
keypad.start(actions)
