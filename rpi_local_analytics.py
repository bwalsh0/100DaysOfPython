import time
from datetime import datetime
import pytz
import Adafruit_DHT
import RPi.GPIO as GPIO
from RPLCD import CharLCD
import csv
import os

DUTY_CYCLE = [30 * 60, 10 * 60]                     # ROP in minutes, [task1, task2]
LCD_DATA_PINS = [13, 6, 5, 11]
S_PIN, SENSOR, B_PIN = 14, 22, 23       # Sensor signal, sensor data, button pin
DNS_KEYS, DNS_STATE = None, None
counter = 0                             # Units: sec, Max: DUTY_CYCLE[0]

def main():
    global DNS_KEYS
    global DNS_STATE
    with open(r'./private-values/dns-list.txt', 'r') as dnsList:
        DNS_KEYS = [tuple(row.rstrip().split(',')) for row in dnsList.readlines()]
        DNS_STATE = [-1] * len(DNS_KEYS)

    while True:
        print(">> Logging")
        poll_sensor()
        poll_dns()
        hold(counter)              # Hold for 30 min, listen for button down


def poll_sensor():
    temp, humidity = read_sensor()
    timeNow = datetime.now(pytz.timezone('US/Pacific')).strftime("%m/%d/%Y %H:%M")
    print('Temp:{0}\u00b0F Hum:{1}%'.format(temp, humidity), timeNow)
    with open(r'sensor_log.txt', 'a') as log:
        output = str(temp) + ',' + str(humidity) + ',' + timeNow + '\n'
        log.write(output)
        log.close()


def hold(counter: int): 
    while counter <= DUTY_CYCLE[0]:
        if GPIO.input(B_PIN) == GPIO.HIGH:
            trigger_sensor(counter)
            counter += 3
        if counter % DUTY_CYCLE[1] == 0:
            poll_dns()
            counter += len(DNS_KEYS)
        counter += 1
        time.sleep(1)


def read_sensor() -> (float, float):
    humidity, temp = Adafruit_DHT.read_retry(SENSOR, S_PIN)
    temp = temp * 9/5.0 + 32
    if humidity is None and temp is None:
        temp, humidity = -1, -1
        lcd.write_string('Failed to read sensor')
        lcd.clear()
        return temp, humidity
    return round(temp, 2), round(humidity, 2)


def trigger_sensor(counter: int):
    lcd.clear()
    print(">> Reading sensor..")
    lcd.write_string('Reading sensor..')
    temp, humidity = read_sensor()
    lcd.clear()
    lcd.write_string('{0}F, {1}% Hum, c{2}'.format(temp, humidity, counter))
    time.sleep(3)
    lcd.clear()


def poll_dns():
    timeNow = datetime.now(pytz.timezone('US/Pacific')).strftime("%m/%d/%Y %H:%M")
    with open(r'./dns_log.txt', 'a') as dnsOut:
        for index, dns in enumerate(DNS_KEYS):
            status = str(os.system('ping -s 8 -c 8 ' + dns[0]))
            if status == DNS_STATE[index]:
                continue
            DNS_STATE[index] = status
            if status == '0':
                status = 'ON'
            elif status == '256':
                status = 'OFF'
            output = [status] + list(dns) + [timeNow] + ['\n']
            dnsOut.write(','.join(output))


print("Initializing GPIO...")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(B_PIN, GPIO.IN,
        pull_up_down=GPIO.PUD_DOWN)
lcd = CharLCD(pin_rs=26, pin_e=19, pins_data=LCD_DATA_PINS,
            numbering_mode=GPIO.BCM, dotsize=8,
            auto_linebreaks=True,
            cols=16, rows=2)
lcd.clear()
print("GPIO ready, beginning initial poll")

main()
GPIO.cleanup()
# Aiming for overlay graph with Temp vs Time and Hum vs Time
# And overlay with hourly local weather
