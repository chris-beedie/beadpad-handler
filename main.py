import keypad
import time

def key_pressed(mode: int, key: keypad.Keys):
    print(f"START: mode: {mode}, Key: {key}")
    time.sleep(2)
    print(f"END: mode: {mode}, Key: {key}")


keypad.start(key_pressed)

