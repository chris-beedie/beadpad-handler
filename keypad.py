#from pynput import keyboard
import keyboard
from enum import Flag, Enum,auto, IntFlag, IntEnum
from collections import defaultdict

class Key(IntEnum):
    KEY1 = 0
    KEY2 = 1
    KEY3 = 2
    KEY4 = 3
    ROT_BUT = 4
    ROT_CW = 5
    ROT_CCW = 6

class Keypad():

    _SEG_MODE = "mode"
    _SEG_KEY = "key"

    keymap = {
        "terminators": {
            "begin":"q",
            "end":"w"
        },
        "segments":{
            _SEG_MODE:["a","s","d","f"],
            _SEG_KEY:["z","x","c"]
        }
    }
      
    def __init__(self, mode_enum: IntEnum):
        self._mode_enum = mode_enum
        self._segments = defaultdict(int)


    def _add_hook(self, key, fn, *args, **kwargs):

        def _add_hook_wrap(e):
            if e.event_type == keyboard.KEY_DOWN:
                return fn(*args, **kwargs)
        
        keyboard.hook_key(key, _add_hook_wrap)


    def start(self):
        
        terminators = self.keymap["terminators"]
        self._add_hook(terminators["begin"], self.sequence_begin)     
        self._add_hook(terminators["end"], self.sequence_complete)    

        segments = self.keymap["segments"]
        for segment_name, keys in segments.items():
            for key_index, key in enumerate(keys):
                self._add_hook(key, self.sequence_update, segment_name, key_index)    

        print("Hook Started...")
        keyboard.wait()

    def sequence_begin(self):
        print("CLEARING")
        self._segments.clear()


    def sequence_update(self, segment_name, bit_number):
        self._segments[segment_name] += 2**bit_number
        print("UPDATING:",segment_name, bit_number)


    def sequence_complete(self):
        print("COMPLETING")
        mode = self._mode_enum(self._segments[self._SEG_MODE])
        key = Key(self._segments[self._SEG_KEY])

        print(mode, key)
