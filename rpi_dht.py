import sys
import Adafruit_DHT

pin = 23 # GPIO 23

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23)

temperature = temperature * 9/5.0 + 32

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Sensor/pin detected but reading failed')
    sys.exit(1)

# wip room humidity/temp monitor & controller
# uses Adafruit DHT library: https://github.com/adafruit/Adafruit_Python_DHT
