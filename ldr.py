from sensor import sensor
import time
import RPi.GPIO as GPIO

class ldr(sensor):

    def __init__(obj,type,dt,pin,active):

        super().__init__(type,dt,pin,active)

    def lux_log_aproximation(obj,x,lux_ref):
        import numpy as np
        a = -1916.05691863903
        b = 28909.65249109060
        lux_apr = a*np.log(x)+b
        if (lux_apr < 0): lux_apr = 0.00;
        lux_per = (lux_apr*100)/lux_ref
        if (lux_per > 100): lux_per = 100.00;
        return round(lux_per,2)

    def read_snsr(obj):
        # SETMODE
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        med = 0; GPIO_PIN = obj.pin
        GPIO.setup(GPIO_PIN,GPIO.OUT)
        GPIO.output(GPIO_PIN,GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(GPIO_PIN,GPIO.IN)
        while (GPIO.input(GPIO_PIN)==GPIO.LOW):
            med+=1
            if (med >= 3570074.133333333333):
                break
        return obj.lux_log_aproximation(med,17823)
