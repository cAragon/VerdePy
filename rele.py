import datetime

import RPi.GPIO as GPIO

class rele:

# CONSTRUTOR ###################################################################

    def __init__(obj,name,is_active,is_periodic,dt_act,dt_inact,pin):
        obj.name         = name
        obj.is_active    = is_active
        obj.is_periodic  = is_periodic
        obj.stat         = 'DEACTIVATED'
        obj.dt_act       = datetime.datetime.strptime(dt_act  , '%H:%M:%S')
        obj.dt_inact     = datetime.datetime.strptime(dt_inact, '%H:%M:%S')
        obj.next_act     = datetime.datetime.now()
        obj.pin          = pin

# METHODS ######################################################################

    def deactivate(obj):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(obj.pin,GPIO.OUT)
        GPIO.output(obj.pin,True)

    def activate(obj):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(obj.pin,GPIO.OUT)
        GPIO.output(obj.pin,False)

    def get_name(obj):
        return obj.name

    def get_is_active(obj):
        return obj.is_active

    def get_is_periodic(obj):
        return obj.is_periodic

    def get_stat(obj):
        return obj.stat

    def get_dt_act(obj):
        return obj.dt_act

    def get_dt_inact(obj):
        return obj.dt_inact

    def get_next_act(obj):
        return obj.next_act

    def get_pin(obj):
        return obj.pin

    def set_name(obj,name):
        obj.name = name

    def set_is_active(obj,is_active):
        obj.is_active = is_active

    def set_is_periodic(obj,is_periodic):
        obj.is_periodic = is_periodic

    def set_stat(obj,stat):
        obj.stat = stat

    def set_dt_act(obj,dt_act):
        obj.dt_act = dt_act

    def set_dt_inact(obj,dt_inact):
        obj.dt_inact = dt_inact

    def set_next_act(obj,next_act):
        obj.next_act = next_act

    def set_pin(obj,pin):
        obj.pin = pin
