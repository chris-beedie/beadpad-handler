import keyboard
from enum import IntEnum
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

    keymap = {
        "terminators": {
            "begin":"q",
            "end":"w"
        },
        "segments":{
            "mode":["a","s","d","f"],
            "key":["z","x","c"]
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
        self._add_hook(terminators["begin"], self._sequence_begin)     
        self._add_hook(terminators["end"], self._sequence_complete)    

        segments = self.keymap["segments"]
        for segment_name, keys in segments.items():
            for key_index, key in enumerate(keys):
                self._add_hook(key, self._sequence_update, segment_name, key_index)    

        print("Hook Started...")
        keyboard.wait()


    def _sequence_begin(self):
        print("CLEARING")
        self._segments.clear()


    def _sequence_update(self, segment_name, bit_number):
        self._segments[segment_name] += 2**bit_number
        print("UPDATING:",segment_name, bit_number)


    def _sequence_complete(self):
        print("COMPLETING")
        mode = self._mode_enum(self._segments["mode"])
        key = Key(self._segments["key"])

        print(mode, key)
