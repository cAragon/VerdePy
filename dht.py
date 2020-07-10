from sensor import sensor

import Adafruit_DHT

class dht(sensor):

    def __init__(obj,type,dt,pin,active):

        super().__init__(type,dt,pin,active)

    def read_snsr(obj):
        DHT11_SENSOR = Adafruit_DHT.DHT11; DHT11_PIN = obj.pin
        umid, temp = Adafruit_DHT.read(DHT11_SENSOR, DHT11_PIN)
        if (obj.type == 'temp'):
            if (temp is not None):
                return temp
            else:
                return -9.99
        if (obj.type == 'umid'):
            if (umid is not None):
                return umid
            else:
                return -9.99
