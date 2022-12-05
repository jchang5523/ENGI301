import time

import Adafruit_BBIO.SPI  as SPI
import Adafruit_BBIO.GPIO as GPIO

import time
import board
import busio
import adafruit_veml7700

i2c = busio.I2C(board.SCL, board.SDA)
veml7700 = adafruit_veml7700.VEML7700(i2c)
#print("Ambient light:", veml7700.light)
#print("Lux:", veml7700.lux)

# ------------------------------------------------------------------------
# Global Variables    
# -----------------------------------------------------------------------
# Interrupt pin on the PocketBeagle for the Motion Click
PIR_pin = "P1_02"

# Time delay between SPI writes
timeDelay     = 0.00006


# ------------------------------------------------------------------------
# Demo Functions
# ------------------------------------------------------------------------

def ledStringOn(spi_bus):
    """Generate colors on LED string based on brightness of room"""
    if veml7700.lux < 100
        spi_bus.writebytes([0x8B, 0x0, 0x0]) #red
        time.sleep(timeDelay)
    else if veml7700.lux < 250
        spi_bus.writebytes([0x0, 0x0, 0xFF]) #blue
        time.sleep(timeDelay)
    else if veml7700.lux < 500
        spi_bus.writebytes([0x22, 0x8B, 0x22]) #green
        time.sleep(timeDelay)
    else if veml7700.lux < 750
        spi_bus.writebytes([0xFF, 0x8C, 0x0]) #orange
        time.sleep(timeDelay)
    else 
        spi_bus.writebytes([0xF8, 0xF8, 0xFF]) #white
        time.sleep(timeDelay)



def ledStringOff(spi_bus):
    """Turn off the LED String"""
    spi_bus.writebytes([0, 0, 0])
    time.sleep(timeDelay)

 
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
 
    # Set up interrupt
    GPIO.setup(PIR_pin, GPIO.IN)

    # Open the SPI port
    spi = SPI.SPI(1, 0)

    # Main loop to turn on/off the LED string
    while(True):
       if GPIO.input(PIR_pin):
           ledStringOn(spi)
       else:
           ledStringOff(spi)

    # Clean up the SPI and GPIO
    spi.close()
    GPIO.cleanup()



