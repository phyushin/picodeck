# PicoDeck
Macropad functionality akin to streamdeck using a pico rgb keyboard

# Getting Started
Taken from the Pimoroni PMK circuit python [repo](1):
"...
You'll need to grab the latest version of Adafruit's Raspberry Pi Pico-flavoured CircuitPython, from the link below.

[Download the Adafruit CircuitPython binary for Raspberry Pi Pico](2)

Unplug your Pi Pico's micro USB cable, press and hold the BOOTSEL button on the top of Pi Pico while plugging the micro USB cable back into your computer to mount it as a drive (it should show up as RPI-RP2 or something similar).

Drag and drop the adafruit-circuitpython-raspberry_pi_pico-en_US-XXXXX.uf2 file that you downloaded onto the drive and it should reboot and load the CircuitPython firmware. The drive should now show up as CIRCUITPY.
..."

Once you've done this drag the `code.py` file and the `lib` folder onto the `CIRCUITPY` and off you go!


# ToDo
- [ ] Figure out interrupts to _thread_ logic and lights separately
- [ ] Have a txt file will button config
- [ ] Have orientation options ** this will be a bit weird
- [ ] bit mask config row for _folders_


[1]:https://github.com/pimoroni/pmk-circuitpython
[2]:https://circuitpython.org/board/raspberry_pi_pico/