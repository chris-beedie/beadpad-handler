from enum import IntEnum, Enum, auto
from pynput import keyboard
from threading import Thread

class Key(Enum):
    KEY1 = auto()
    KEY2 = auto()
    KEY3 = auto()
    KEY4 = auto()
    ROT_BUT = auto()
    ROT_CW = auto()
    ROT_CCW = auto()

class KeypadError(Exception):
    pass

class Keypad:

    _keys = {
        Key.KEY1: '<F1>',
        Key.KEY2: '<F2>',
        Key.KEY3: '<F3>',
        Key.KEY4: '<F4>',
        Key.ROT_BUT: '<F5>',
        Key.ROT_CCW: '<F6>',
        Key.ROT_CW: '<F7>',
    }

    _mode_modifiers = [
        '<ctrl>', 
        '<shift>',
        '<ctrl>+<shift>'
    ]

    def __init__(self, mode_enum: IntEnum):
        self._mode_enum = mode_enum
        

    def _build_hotkeys(self):

        try:
            return { 
                f"{self._mode_modifiers[mode.value]}+{key_value}": self._handle_key(mode, key) 
                for mode in self._mode_enum 
                for key, key_value in self._keys.items() 
            }
        except IndexError:
            raise KeypadError(f"Too many modes defined, max={len(self._mode_modifiers)}")


    def _handle_key(self, mode: IntEnum, key: Key):
        def _handle_key_wrap():
            Thread(target=self._callback, args=(mode, key)).start()
        return _handle_key_wrap  


    def start(self, callback):
        
        self._callback = callback

        print ("Keyhooks Starting...")

        with keyboard.GlobalHotKeys(self._build_hotkeys()) as h:
            self._listener = h
            h.join()


    def stop(self):
        print ("Keyhooks Ending...")
        
        if self._listener:
            self._listener.stop()
