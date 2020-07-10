import datetime

import ops_time

class sensor:

# CONSTRUTOR ###################################################################

    def __init__(obj,type,dt,pin,active):
        obj.type      = type
        obj.dt        = datetime.datetime.strptime(dt,'%H:%M:%S')
        obj.pin       = pin
        obj.active    = active
        obj.read      = datetime.datetime.now()
        obj.stat      = 'INACTIVE'

# METHODS ######################################################################

    def get_type(obj):
        return obj.type

    def get_dt(obj):
        return obj.dt

    def get_pin(obj):
        return obj.pins

    def get_active(obj):
        return obj.active

    def get_read(obj):
        return obj.read

    def get_stat(obj):
        return obj.stat

    def set_type(obj,type):
        obj.type = type

    def set_dt(obj,dt):
        obj.dt = dt

    def set_pin(obj,pin):
        obj.pin = pin

    def set_active(obj,active):
        obj.active = active

    def set_read(obj,read):
        obj.read = read

    def set_stat(obj,stat):
        obj.stat = stat
