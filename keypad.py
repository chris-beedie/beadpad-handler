from enum import Enum, auto
from pynput import keyboard
from threading import Thread

# Using enum class create enumerations
class Keys(Enum):
    KEY1 = auto()
    KEY2 = auto()
    KEY3 = auto()
    KEY4 = auto()
    ROT_BUT = auto()
    ROT_CW = auto()
    ROT_CCW = auto()

keys = {
    Keys.KEY1: '<F1>',
    Keys.KEY2: '<F2>',
    Keys.KEY3: '<F3>',
    Keys.KEY4: '<F4>',
    Keys.ROT_BUT: '<F5>',
    Keys.ROT_CCW: '<F6>',
    Keys.ROT_CW: '<F7>',
}

mode_modifiers = [
    '<ctrl>', 
    '<shift>',
    '<ctrl>+<shift>'
]

def _build_hotkeys():

    #hks = {}

    # for mode_idx, mode_mod in enumerate(mode_modifiers):
    #     for key, key_value in keys.items():
    #         print(f"{mode_idx}/{key.name}: \t{mode_mod}+{key_value}")
    #         hks[f"{mode_mod}+{key_value}"] = handle_key(mode_idx,key)

    #return hks

    return { 
        f"{mode_mod}+{key_value}": _handle_key(mode_idx,key) 
            for mode_idx, mode_mod in enumerate(mode_modifiers) 
            for key, key_value in keys.items() 
        }

def _handle_key(mode: int, key: Keys):
    def _handle_key_wrap():
        Thread(target=_callback, args=(mode, key)).start()
    return _handle_key_wrap  


def start(callback):
    global _callback    
    _callback = callback

    print ("Keyhooks Starting...")

    hotkeys = _build_hotkeys()

    global _listener
    with keyboard.GlobalHotKeys(hotkeys) as h:
        _listener = h
        h.join()


def stop():
    print ("Keyhooks Ending...")
    global _listener
    _listener.stop()




# q = queue.Queue()

#         with GlobalHotKeys({
#                 '<ctrl>+<shift>+a': lambda: q.put('a'),
#                 '<ctrl>+<shift>+b': lambda: q.put('b'),
#                 '<ctrl>+<shift>+c': lambda: q.put('c')}):
#             notify('Press <ctrl>+<shift>+a')
#             self.assertEqual('a', q.get())

#             notify('Press <ctrl>+<shift>+b')
#             self.assertEqual('b', q.get())

#             notify('Press <ctrl>+<shift>+c')
#             self.assertEqual('c', q.get())