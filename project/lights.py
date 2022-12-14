"""
--------------------------------------------------------------------------
Room Welcoming System
--------------------------------------------------------------------------
License:   
Copyright 2022 <Jonathan Chang>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the following hardware components to make a room welcoming system:  
  - LED light strip
  - PIR sensor
  - Light sensor
  - USB speaker

Requirements:
See https://www.hackster.io/jchang5523/room-welcoming-system-fd27b1

Uses:
This project should welcome one home by playing a welcome sound and turn on LED lights on a ceiling whenever someone enters and turnthem off when and IR sensor is triggered. 
The LEDs should also automatically adjust their color based on the brightness of the room and a speaker should play a sound file.

"""


# Uses LED strip light 
#    - connection / setup described in https://www.hackster.io/hs49/clap-on-led-light-strip-6bed85



import time

import Adafruit_BBIO.SPI  as SPI
import Adafruit_BBIO.GPIO as GPIO

import time
import board
import busio
import vlc
import adafruit_veml7700



# ------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------

LED_STR_LEN = 240     # Length of the LED string



# ------------------------------------------------------------------------
# Global Variables    
# -----------------------------------------------------------------------


#Room welcoming class
class RoomWelcomer():
    
    led_strip_light = None
    light_sensor    = None
    motion_sensor   = None
    song            = None
    
    def __init__(self, led_strip_light="P1_08", light_sensor_bus=[board.SCL, board.SDA], motion_sensor_pin="P1_02", song="P1_29"):
        self.led_strip_light = led_strip_light
        i2c = busio.I2C(board.SCL, board.SDA)
        self.light_sensor    = adafruit_veml7700.VEML7700(i2c)
        self.motion_sensor   = motion_sensor_pin
        self.song            = song
        self.ledstringOff()
        self.setup()

    # End def
        
    def ledStringOff(self):
        """Turn off the LED String"""
        print("Turn LED Strip Off")
        for i in range(STR_LEN):
            leds = [(0, 0, 0)] * STR_LEN
        client.put_pixels(leds, channel=0): #sends color array over
        print ('not connected')
    # End def

    
    def play_song(self):
        audio = "var/lib/cloud9/ENGI301/project/testaudio.mp3"
        p = vlc.Mediaplayer(audio)
        p.play()
        print("Play song")
        
    # End def

    
    def setup(self):
        # Setup Motion sensor
        GPIO.setup(self.motion_sensor, GPIO.IN)

        # Setup light sensor    
        GPIO.setup(self.light_sensor, GPIO.IN)
        
        #setup LED strip
        GPIO.setup(self.led_strip_light, GPIO.IN)

        #setup speaker
        GPIO.setup(self.song, GPIO.IN)
    # End def


    def cleanup(self):
        # Clean up the GPIOs
        GPIO.cleanup()
        
        # Make sure the LED strip is off
        self.ledStringOff()
    # End def

    
        
    def ledStringOn(self.light_sensor, spi_bus):
        """Generate colors on LED string based on brightness of room"""
        if veml7700.lux < 100
            for i in range(STR_LEN):
                leds = [(255, 0, 0)] * STR_LEN #red
                client.put_pixels(leds, channel=0) #sends color array over
            time.sleep(timeDelay)
        else if veml7700.lux < 250
            for i in range(STR_LEN):
                leds = [(0, 0, 255)] * STR_LEN #blue
                client.put_pixels(leds, channel=0)
            time.sleep(timeDelay)
        else if veml7700.lux < 500
            for i in range(STR_LEN):
                leds = [(0, 204, 102)] * STR_LEN #green
                client.put_pixels(leds, channel=0) 
            time.sleep(timeDelay)
        else if veml7700.lux < 750
            for i in range(STR_LEN):
                leds = [(255, 128, 0)] * STR_LEN #orange
                client.put_pixels(leds, channel=0) 
            time.sleep(timeDelay)    
        else
            for i in range(STR_LEN):
                leds = [(255, 255, 255)] * STR_LEN #white
                client.put_pixels(leds, channel=0) 
            time.sleep(timeDelay)
            
            
        def run(self):
        # Main loop to turn on/off the LED string
            while(True):
               if GPIO.input(self.motion_sensor):
                   if power: #If power is already on, turn off LEDs
                        self.ledStringOff(spi)
                        power = False
                        sd.sleep(300)
                    else:
                        self.ledStringOn(spi)
                        power = True
                        self.play_song
                        sd.sleep(300)
        # End def
# End class


 
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    # Instantiate the RoomWelcomer
    welcome = RoomWelcomer()
    
    try:
        welcome.run()
    except KeyboardInterrupt:
        pass
    
    welcome.cleanup()
    
    print("Exiting")
