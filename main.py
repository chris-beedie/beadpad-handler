from keypad import Keypad, Key
import time

from enum import IntEnum

import soco

SONOS_IP = '192.168.50.250'

sonos = soco.SoCo(SONOS_IP)

def sonos_toggle_play():

    if sonos.get_current_transport_info()['current_transport_state'] == 'PLAYING':
        sonos.pause()
    else:
        sonos.play()

def sonos_volume_up():
    sonos.volume += 1

def sonos_volume_down():
    sonos.volume -= 1

def sonos_mute():
    sonos.mute = not sonos.mute


class Mode(IntEnum):
    Media = 0
    Sonos = 1
    Another = 2
    AndAnother = 3
    YetAnother = 4
    HowMany =5
    MaybeOne = 6
    OkLastOne = 7

keypad = Keypad(Mode)


def key_pressed(mode: Mode, key: Key):
    print(f"START: mode: {mode.name}, Key: {key}")
    time.sleep(2)
    print(f"END: mode: {mode.name}, Key: {key}")


actions = {

    Mode.Media: { 
        Key.KEY1: lambda: keypad.send('ctrl+c'),
        Key.KEY2: lambda: keypad.send('ctrl+v'),
        Key.ROT_BUT: lambda: keypad.send('volume mute'),
        Key.ROT_CW: lambda: keypad.send('volume up'),
        Key.ROT_CCW: lambda: keypad.send('volume down')
    },
    Mode.Sonos: {
        Key.KEY1: sonos_toggle_play,
        Key.KEY2: lambda: sonos.previous(),
        Key.KEY3: lambda: sonos.next(),
        Key.ROT_BUT: sonos_mute,
        Key.ROT_CW: sonos_volume_up,
        Key.ROT_CCW: sonos_volume_down
        
    },
    Mode.Another: {
        Key.KEY2: lambda: print("M3K2"),
        Key.KEY3: lambda: print("M3K3"),
        Key.KEY4: lambda: print("M3K4"),
        Key.ROT_BUT: lambda: print("M3KRB"),
        Key.ROT_CCW: lambda: print("M3KRCCW")
    }
}


#keypad.start(key_pressed)
keypad.start(actions)