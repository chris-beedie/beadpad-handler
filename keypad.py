import keyboard
from enum import IntEnum
from collections import defaultdict
from typing import Union
from threading import Thread

#TODO
#add logger


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
        "terminator": "q",
        "segments":{
            "mode":["a","s","d"],
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


    def start(self, handler: Union[dict, callable]):
        
        self._callback = handler if callable(handler) else self._handle_key(handler)

        #add hooks
        self._add_hook(self.keymap["terminator"], self._complete)        

        segments = self.keymap["segments"]
        for segment_name, keys in segments.items():
            for index, key in enumerate(keys):
                self._add_hook(key, self._set_segment_bit, segment_name, index)    

        print("Hook Started...") #TODO - LOG
        keyboard.wait()



    def _set_segment_bit(self, segment_name, bit_number):
        self._segments[segment_name] += 2**bit_number


    def _complete(self):
        try:
            mode = self._mode_enum(self._segments["mode"])
            key = Key(self._segments["key"])
        except ValueError as e:
            print(e) #TODO - LOG
            return
        finally:
            self._segments.clear()

        Thread(target=self._callback, args=(mode, key)).start()


    def _handle_key(self, actions: dict):
        def _handle_key_wrap(mode: self._mode_enum, key: Key):
        
            action = (
                actions
                .get(mode,{})
                .get(key,lambda: print(f"no action defined for '{key.name}' in mode '{mode.name}'")) #TODO - LOG
            )
            
            action()

        return _handle_key_wrap



    