from test import Keypad, Key
import time

from enum import IntEnum


class Mode(IntEnum):
    Teams = 0
    Sonos = 1
    Another = 2
    AndAnother = 3




def send_copy():
    keypad.sender.tap('<ctrl>+c')

def send_paste():
    keypad.sender.tap('<ctrl>+v')


# def key_pressed(mode: Mode, key: Key):
    
#     print(f"START: mode: {mode.name}, Key: {key}")
#     time.sleep(2)
#     print(f"END: mode: {mode.name}, Key: {key}")

keypad = Keypad(Mode)


#keypad.start(actions)

#keypad.start(key_pressed)




# names = ['newname1', 'newname2']
# ExistingEnum = IntEnum('KeypadMessage', names)

# for i in ExistingEnum:
#     print(i)



keymap = {
    "terminators":["q","w"],
    "data":{
        "mode":["a","s","d"],
        "button":["z","x","c","d"]
    }
}


parts = keymap['data']

new_parts = {}
for k,v in parts.items():
    new_parts[k] = len(v)

new_new_parts = {name:len(bits) for (name,bits) in keymap['data'].items()}

print(new_new_parts)



# keypad.message_handler(MessageBit.START)
# keypad.message_handler(MessageBit.MODE_1)
# keypad.message_handler(MessageBit.END)

# message_handler(MessageBit.START)
# message_handler(MessageBit.MODE_1)
# message_handler(MessageBit.BUT_0)
# message_handler(MessageBit.END)

# message_handler(MessageBit.START)
# message_handler(MessageBit.BUT_1)
# message_handler(MessageBit.END)

# message_handler(MessageBit.START)
# message_handler(MessageBit.MODE_0)
# message_handler(MessageBit.BUT_0)
# message_handler(MessageBit.BUT_1)
# message_handler(MessageBit.END)

# message_handler(MessageBit.START)
# message_handler(MessageBit.MODE_0)
# message_handler(MessageBit.MODE_1)
# message_handler(MessageBit.BUT_2)
# message_handler(MessageBit.END)
















# from keypad import Keypad, Key
# import time

# from enum import IntEnum


# class Mode(IntEnum):
#     Teams = 0
#     Sonos = 1
#     Another = 2




# def send_copy():
#     keypad.sender.tap('<ctrl>+c')

# def send_paste():
#     keypad.sender.tap('<ctrl>+v')


# # def key_pressed(mode: Mode, key: Key):
    
# #     print(f"START: mode: {mode.name}, Key: {key}")
# #     time.sleep(2)
# #     print(f"END: mode: {mode.name}, Key: {key}")

# keypad = Keypad(Mode)
# keypad.start(actions)

# #keypad.start(key_pressed)

