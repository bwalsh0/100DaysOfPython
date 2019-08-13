import time
import Adafruit_DHT
import RPi.GPIO as GPIO
from RPLCD import CharLCD
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

POLL_RATE = 5 * 60     # ROP in minutes

lcd_rs = 26
lcd_en = 19
lcd_data = [13, 6, 5, 11]

sensor = 22     # sensor model
sPin = 14        # sensor signal gpio pin
bPin = 23     # toggle button gpi pin

GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

lcd = CharLCD(pin_rs=lcd_rs, pin_e=lcd_en, pins_data=lcd_data,
numbering_mode=GPIO.BCM,
auto_linebreaks=True,
cols=16, rows=2, dotsize=8)

lcd.clear()


def main():
    while True:
        poll_sensor()
        idle_sensor()   # Hold for 30 min, listen for button down
        print("Looped")
    # average_rop()


def poll_sensor():
    timeNow = datetime.now().strftime("%m/%d/%Y %H:%M")
    # lcd.write_string('Polling ROP...')
    humidity, temp = Adafruit_DHT.read_retry(sensor, sPin)
    temp = temp * 9/5.0 + 32
    time.sleep(0.5)

    if humidity is not None and temp is not None:
        print('Temp:{0:0.1f} Hum:{1:0.1f}%'.format(temp, humidity), timeNow)
        time.sleep(5)
    else:
        temp, humidity = -1, -1
        lcd.write_string('Failed to read sensor')
        print("Failed to read sensor at", timeNow)
        time.sleep(5)
    lcd.clear()

    store_rop(temp, humidity, timeNow)


def store_rop(temp: float, hum: float, time: str):
    with open(r'sensor_log.txt', 'a') as log:
        output = str(temp) + ',' + str(hum) + ',' + time + '\n'
        log.write(output)


def idle_sensor():
    counter = 0

    while counter <= POLL_RATE:
        if GPIO.input(bPin) == GPIO.HIGH:
            print("Pressed")
            read_sensor(counter)

        counter += 1
        time.sleep(1)


def read_sensor(counter: int):
    lcd.clear()
    lcd.write_string('Reading sensor..')
    humidity, temp = Adafruit_DHT.read_retry(sensor, sPin)
    temp = temp * 9/5.0 + 32
    time.sleep(0.5)

    lcd.clear()
    if humidity is not None and temp is not None:
        # print('Temp:{0:0.1f}  Hum:{1:0.1f}%'.format(temp, humidity))
        lcd.write_string('T:{0:0.1f}F H:{1:0.1f}%, c{2}'.format(temp, humidity, counter))
        time.sleep(5)
    else:
        lcd.write_string('Failed to read sensor')
        time.sleep(1)
    lcd.clear()


main()
GPIO.cleanup()
