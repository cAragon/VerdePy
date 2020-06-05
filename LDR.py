import datetime, time, verde3_tools as tools,

import # random

import RPi.GPIO as GPIO

class LDR:

    def __init__(obj,name,dt,active):
        obj.name      = name
        obj.dt        = datetime.datetime.strptime(dt,'%H:%M:%S')
        obj.active    = active
        obj.dispatch  = datetime.datetime.now()+obj.toDelta(obj.dt.time())
        obj.stat      = 'INACTIVE'

    # SENSOR SETUP
    def init(obj):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    # SENSOR READ
    def read(obj):
        med = 0; GPIO_PIN = 4
        GPIO.setup(GPIO_PIN,GPIO.OUT)
        GPIO.output(GPIO_PIN,GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(GPIO_PIN,GPIO.IN)
        while (GPIO.input(GPIO_PIN)==GPIO.LOW):
            med+=1
        return med

    # CHECK DATA DISPATCH
    def check_dispatch(obj,snap_dxnry,value):
        if (datetime.datetime.now().time() >= obj.dispatch.time()):
            snap_dxnry['dispatch'] = True
            obj.dispatch = datetime.datetime.now()+obj.toDelta(obj.dt.time())
            tools.append_to_snapshot(snap_dxnry,0,value,obj.toISO8601(datetime.datetime.now()))

    # CHECK SENSOR OPERATION
    def check_op(obj,data_dxnry,snap_dxnry):
        if (obj.active == True):
            if (obj.stat == 'INACTIVE'): obj.stat = 'ACTIVE';
            obj.init()
            value = obj.read()
            # value = random.uniform(150.0,350.0)
            tools.append_lux_to_data_dxnry(data_dxnry,value,obj.toISO8601(datetime.datetime.now()))
            obj.check_dispatch(snap_dxnry,value)
        if (obj.active == False): obj.stat = 'INACTIVE';

    # AUXILIARIES FUNCTIONS
    def toDelta(obj,t):
        return datetime.timedelta(0,t.hour*3600 + t.minute*60 + t.second)

    def toISO8601(obj,t):
        return datetime.datetime.strftime(t,'%Y-%m-%d')+'T'+datetime.datetime.strftime(t,'%H:%M')+'Z'
