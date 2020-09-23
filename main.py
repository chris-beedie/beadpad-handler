
#constants for key?
#export method keypress(mode,key)

#method to override keys/modifiers

#method to start/stop



# print the enum member as a string


import keypad
import time

def key_pressed(mode: int, key: keypad.Keys):
    print(f"START: mode: {mode}, Key: {key}")
    time.sleep(2)
    print(f"END: mode: {mode}, Key: {key}")


keypad.start(key_pressed)

#keypad.build_hotkeys()


#keypad._handle_key(5,keypad.Keys.Key4)







