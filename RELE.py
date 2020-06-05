import datetime, time

import RPi.GPIO as GPIO

class RELE:

# CONSTRUTOR ###################################################################

    def __init__(obj,name,is_active,is_periodic,dt_act,dt_inact,pin):
        obj.name         = name
        obj.is_active    = is_active
        obj.is_periodic  = is_periodic
        obj.stat         = 'INACTIVE'
        obj.dt_act       = datetime.datetime.strptime(dt_act  , '%H:%M:%S')
        obj.dt_inact     = datetime.datetime.strptime(dt_inact, '%H:%M:%S')
        obj.next_act     = datetime.datetime.now()
        obj.pin          = pin

# SETUP ########################################################################

    def init(obj):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(obj.pin,GPIO.OUT)
        GPIO.output(obj.pin,True)

# CHECK OP #####################################################################

    def check_op(obj):
        if (obj.is_active == True):
            if (obj.stat == 'INACTIVE'):
                # obj.init()
                obj.stat = 'ACTIVE'
            # GPIO.output(obj.pin,False)
            if (obj.is_periodic == True):
                if (obj.stat == 'ACTIVE'):
                    dt = obj.next_act + obj.toDelta(obj.dt_act.time())
                    if (datetime.datetime.now().time() >= dt.time()):
                        # GPIO.output(obj.pin,True)
                        obj.stat = 'INACTIVE'
                if (obj.stat == 'INACTIVE'):
                    dt = obj.next_act + obj.toDelta(obj.dt_act.time()) + obj.toDelta(obj.dt_inact.time())
                    if (datetime.datetime.now().time() >= dt.time()):
                        # GPIO.output(obj.pin,False)
                        obj.stat = 'ACTIVE'
                        obj.next_act = dt
        if (obj.is_active == False):
            # GPIO.output(obj.pin,True)
            obj.stat = 'INACTIVE'

# AUX ##########################################################################

    def toDelta(obj,t):
        return datetime.timedelta(0,t.hour*3600 + t.minute*60 + t.second)
