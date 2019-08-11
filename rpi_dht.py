import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
from datetime import datetime

GPIO.setwarnings(False)

lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 11
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

sensor = 22     # sensor model
sPin = 14        # sensor signal gpio pin
bPin = 15     # toggle button gpi pin

GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()


def main():
    while True:
        poll_sensor()
        time.sleep(1800)
    
    # average_rop()

def poll_sensor():
        # bState = GPIO.input(bPin)
        # if bState:
    lcd.message('Reading...')
    time.sleep(0.5)
    lcd.clear()
    humidity, temp = Adafruit_DHT.read_retry(sensor, sPin)
    temp = temp * 9/5.0 + 32
    time.sleep(0.5)

    if humidity is not None and temp is not None:
        print('Temp:{0:0.1f}  Hum:{1:0.1f}%'.format(temp, humidity))
        lcd.message('T:{0:0.1f}F\nH:{1:0.1f}%'.format(temp, humidity))
        time.sleep(5)
    else:
        lcd.message('Failed to read sensor')
        lcd.clear()
        time.sleep(1)
    
    time = datetime.now()
    store_rop(temp, humidity, time)

def store_rop(temp: float, hum: float, time: str):
    with open(r'sensor_log.txt', 'a') as log:
        rop = str(temp) + ',' + str(hum) + ',' + str(time) + '\n'
        log.write(rop)

main()
