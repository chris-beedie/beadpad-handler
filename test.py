#from pynput import keyboard
#import keyboard
from enum import Flag, Enum,auto, IntFlag, IntEnum


class MessageEnum(IntEnum):
    START = 0
    END = 1

class Message:

    _state = 0

    def __init__(self, message_enum: IntEnum, parts: dict, callback: callable):
        self._message_enum = message_enum
        self._callback = callback
        self._decoders = { k:self._decoder(*v) for (k,v) in parts.items() }

    def _decoder(prefix, decoded_enum):

        mask = sum([2**bit.value for bit in message_enum if prefix in bit.name])
        offset = message_enum[prefix+"0"].value

        def _decode(state):

            decoded = (state & mask) >> offset
            return decoded_enum(decoded)

        return _decode

    def begin():
         self._state = 0

    def end():

        decoded_parts = { k:v(self._state) for (k,v) in self._decoders.items() }

        self._callback(decoded_parts)

    def update_state(bit_number:int):
        self._state += 2**bit_number.value

        #call callback with dict of parts, where key is name and value is the enum used


#how doe we let the generic class know about start and end




class Key(IntEnum):
    KEY1 = 0
    KEY2 = 1
    KEY3 = 2
    KEY4 = 3
    ROT_BUT = 4
    ROT_CW = 5
    ROT_CCW = 6

class Keypad():

    class KeypadMessage(IntEnum):
        BUT_0 =  0
        BUT_1 =  1
        BUT_2 =  2
        MODE_0 = 3
        MODE_1 = 4
        MODE_2 = 5

    KEY_PREFIX = "BUT_"
    MODE_PREFIX = "MODE_"

    keymap = {
        "terminators":["q","w"],
        "data":{
            "mode":["a","s","d"],
            "button":["z","x","c", "d"]
        }
    }
   
    




    #we can map the terminators on to the right function

    #we then get bits
    # when we get an end teminator, 
    # we call the call back with a dict where the data has been replaced with a value
    # we still need a way to map that on to the enums 





    def __init__(self, mode_enum: IntEnum):
        self._mode_enum = mode_enum
        # self.key = MessageDecode(MessageBit, Key, self.KEY_PREFIX)
        # self.mode = MessageDecode(MessageBit, self._mode_enum, self.MODE_PREFIX)
    





    def activate(self):

        #print(key.decode(self.state))
        print(self.mode(self.state))

        #print(list(zip(self.keymap,MessageBit)))



    




