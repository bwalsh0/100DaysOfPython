import time
import Adafruit_DHT
import RPi.GPIO as GPIO
from RPLCD import CharLCD
from datetime import datetime
import pytz

POLL_RATE = 30 * 60     # ROP in minutes
LCD_DATA_PINS = [13, 6, 5, 11]
S_PIN, SENSOR, B_PIN = 14, 22, 23   # Sensor signal, sensor data, button pin

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(B_PIN, GPIO.IN,
           pull_up_down=GPIO.PUD_DOWN)

lcd = CharLCD(pin_rs=26, pin_e=19, pins_data=LCD_DATA_PINS,
              numbering_mode=GPIO.BCM, dotsize=8,
              auto_linebreaks=True,
              cols=16, rows=2)
lcd.clear()


def main():
    while True:
        poll_sensor()
        idle_sensor()   # Hold for 30 min, listen for button down


def poll_sensor():
    temp, humidity = read_sensor()
    timeNow = datetime.now(pytz.timezone('US/Pacific')).strftime("%m/%d/%Y %H:%M")
    print('Temp:{0}\u00b0F Hum:{1}%'.format(temp, humidity), timeNow)
    with open(r'sensor_log.txt', 'a') as log:
        output = str(temp) + ',' + str(humidity) + ',' + timeNow + '\n'
        log.write(output)
        log.close()


def idle_sensor():
    counter = 0
    while counter <= POLL_RATE:
        if GPIO.input(B_PIN) == GPIO.HIGH:
            trigger_sensor(counter)
        counter += 1
        time.sleep(1)


def read_sensor() -> (float, float):
    NUM_SAMPLES = 3.0
    tSample, hSample = [], []

    # Get avg. from multiple reads
    for sample in range(NUM_SAMPLES):
        humidity, temp = Adafruit_DHT.read_retry(SENSOR, S_PIN)
        temp = temp * 9/5.0 + 32
        time.sleep(0.5)
        if humidity is None and temp is None:
            temp, humidity = -1, -1
            lcd.write_string('Failed to read sensor')
            time.sleep(2)
            lcd.clear()
            return temp, humidity
        tSample.append(temp)
        hSample.append(humidity)

    temp, humidity = sum(tSample) / NUM_SAMPLES, sum(hSample) / NUM_SAMPLES
    temp = round(temp, 2)
    humidity = round(humidity, 2)

    return temp, humidity


def trigger_sensor(counter: int):
    lcd.clear()
    print(">> Reading sensor..")
    lcd.write_string('Reading sensor..')
    temp, humidity = read_sensor()
    lcd.clear()
    lcd.write_string('{0}F, {1}% Hum, c{2}'.format(temp, humidity, counter))
    time.sleep(5)
    lcd.clear()


main()
GPIO.cleanup()
