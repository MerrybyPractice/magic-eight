import board
import random
import time
from digitalio import DigitalInOut, Direction
import neopixel
import adafruit_rgbled

# ['__class__', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'ACCELEROMETER_INTERRUPT', 'ACCELEROMETER_SCL', 'ACCELEROMETER_SDA', 'AUDIO', 'BUTTON_A', 
# 'BUTTON_B', 'D0', 'D1', 'D10', 'D2', 'D3', 'D35', 'D6', 'D9', 'I2C', 'L', 'LIGHT', 'MICROPHONE_CLOCK', 'MICROPHONE_DATA', 
# 'MISO', 'MOSI', 'NEOPIXEL', 'POWER_SWITCH', 'RX', 'SCK', 'SCL', 'SDA', 'SLIDE_SWITCH', 'SPEAKER', 'SPEAKER_ENABLE', 'SPI', 'TEMPERATURE', 'TX', 'UART']

color = [(153, 51, 255), (0,0,255), (204,153,255), (0,102,102), (51,153,51), (120,255,102), (255,0,102)]
fortunes = []

#Do the LED Shit again, but this time with NeoPixles
COLOR = color[random.randint(0,(len(color) -1))]

while True: 
  
    time.sleep(1)
    \
    time.sleep(1)


# Need to pull accelerometer data for random seed 
def ball_random(num_shakes): 
    # random.seed(num_shakes)
    ball['color_random'] = random.randint(0, (len(color) -1))
    # ball.fortune_random = random.randint(0, (len(fortunes)-1))

ball_random(1)