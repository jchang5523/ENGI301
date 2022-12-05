"""
--------------------------------------------------------------------------
Room Welcoming System
--------------------------------------------------------------------------
License:   
Copyright 2022 <NAME>

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


Uses:


"""


# Uses LED strip light 
#    - connection / setup described in https://www.hackster.io/hs49/clap-on-led-light-strip-6bed85



import time

import Adafruit_BBIO.SPI  as SPI
import Adafruit_BBIO.GPIO as GPIO

import time
import board
import busio
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
    
    def __init__(self, light_sensor_bus=[board.SCL, board.SDA], motion_sensor_pin="P1_02", song=None):
        self.led_strip_light =
        
        i2c = busio.I2C(board.SCL, board.SDA)
        self.light_sensor    = adafruit_veml7700.VEML7700(i2c)

        self.motion_sensor   = motion_sensor_pin
        
        self.song            = song
        
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
        print("Play song")

    # End def
    

    def run(self):
        # Main loop to turn on/off the LED string
        while(True):
           if GPIO.input(self.motion_sensor):
               self.ledStringOn(spi)
           else:
               self.ledStringOff(spi)
        
    # End def

    
    def setup(self):
        # Setup Motion sensor
        GPIO.setup(self.motion_sensor, GPIO.IN)

        # Setup LED Strip light        
        
    
    # End def


    def cleanup(self):
        # Clean up the GPIOs
        GPIO.cleanup()
        
        # Make sure the LED strip is off
        self.ledStringOff()

    # End def

    
    # See example code 
        
    def ledStringOn(spi_bus):
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
