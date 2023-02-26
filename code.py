from pmk.platform.RGBKeypadBase import RGBKeypadBase as Hardware
from pmk import PMK

import _thread

import time
import board
import digitalio

import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

def initialise(init):
    if not init:
        init = True
        i = 0
        while i < 3:
            pmk.keys[i].set_led(255,255,255)
            time.sleep(1)
            i = 1 + 1
        while i > 0:
            pmk.keys[i].set_led(0,0,0)
            sleep(1)
            i = i -1
            
            
        
pmk = PMK(Hardware())
keys = pmk.keys
speed = 1
init = False

key = keys[0]
mode_mask = 0x0 # binary mask

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
keymap =    [Keycode.ZERO,
             Keycode.ONE,
             Keycode.TWO,
             Keycode.THREE,
             Keycode.FOUR,
             Keycode.FIVE,
             Keycode.SIX,
             Keycode.SEVEN,
             Keycode.EIGHT,
             Keycode.NINE,
             Keycode.A,
             Keycode.B,
             Keycode.C,
             Keycode.D,
             Keycode.E,
             Keycode.F]

for key in keys:
    @pmk.on_press(key)
    def press_handler(key):
        if (key.number < 4):
            keycode = keymap[key.number]
            keyboard.send(keycode)
        else:
            keycode = keymap[key.number]
            keyboard.send(keycode)

        if (led.value):
            pmk.keys[key.number].set_led(0,0,0)
            led.value = False
        else:
            pmk.keys[key.number].set_led(255,0,0)
            led.value = True

while True:
   # initialise(init)
    pmk.update()
