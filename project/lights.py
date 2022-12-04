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
timeDelay     = 0.00005


# ------------------------------------------------------------------------
# Demo Functions
# ------------------------------------------------------------------------

def ledStringRandom(spi_bus):
    """Generate random colors on LED string"""
    spi_bus.writebytes([0xFF, 0, 0])
    time.sleep(timeDelay)
    
    spi_bus.writebytes([0, 0xFF, 0])
    time.sleep(timeDelay)
# End def


def ledStringOff(spi_bus):
    """Turn off the LED String"""
    spi_bus.writebytes([0, 0, 0])
    time.sleep(timeDelay)
# End def

 
# ------------------------------------------------------------------------
# Main script
# -------------------------------------------------------------- ----------

if __name__ == '__main__':
 
    # Set up interrupt
    GPIO.setup(PIR_pin, GPIO.IN)

    # Open the SPI port
    spi = SPI.SPI(1, 0)

    # Main loop to turn on/off the LED string
    while(True):
       if GPIO.input(PIR_pin):
           ledStringRandom(spi)
       else:
           ledStringOff(spi)

    # Clean up the SPI and GPIO
    spi.close()
    GPIO.cleanup()

