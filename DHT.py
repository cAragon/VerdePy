import datetime, time, verde3_tools as tools, random

import Adafruit_DHT

class DHT:

# CONSTRUTOR ###################################################################

    def __init__(obj,name,dt_t,dt_h,active_t,active_h):
        obj.name = name
        obj.dt = [datetime.datetime.strptime(dt_t,'%H:%M:%S'),
                  datetime.datetime.strptime(dt_h,'%H:%M:%S')]
        obj.active = [active_t,
                      active_h]
        obj.dispatch = [datetime.datetime.now()+obj.toDelta(obj.dt[0].time()),
                        datetime.datetime.now()+obj.toDelta(obj.dt[1].time())]
        obj.stat = ['INACTIVE',
                    'INACTIVE']

# READ  ########################################################################

    def read(obj):
        DHT11_SENSOR = Adafruit_DHT.DHT11
        DHT11_PIN = 17
        humidity, temperature = Adafruit_DHT.read(DHT11_SENSOR, DHT11_PIN)
        if (humidity is not None and temperature is not None):
            return [humidity,temperature]
        else:
            return [999.99,999.99]

# CHECK DISPATCH ###############################################################

    def check_dispatch(obj,value,snap_dxnry):
        if (datetime.datetime.now().time() >= obj.dispatch[0].time()):
            snap_dxnry['dispatch'] = True
            obj.dispatch[0] = datetime.datetime.now()+obj.toDelta(obj.dt[0].time())
            tools.append_to_snapshot(snap_dxnry,1,value[0],obj.toISO8601(datetime.datetime.now()))
        if (datetime.datetime.now().time() >= obj.dispatch[1].time()):
            snap_dxnry['dispatch'] = True
            obj.dispatch[1] = datetime.datetime.now()+obj.toDelta(obj.dt[1].time())
            tools.append_to_snapshot(snap_dxnry,2,value[1],obj.toISO8601(datetime.datetime.now()))

# CHECK OP #####################################################################

    def check_op(obj,data_dxnry,snap_dxnry):
        if (obj.active[0] == True or obj.active[1] == True):
            if (obj.stat[0] == 'INACTIVE'): obj.stat[0] = 'ACTIVE';
            if (obj.stat[1] == 'INACTIVE'): obj.stat[1] = 'ACTIVE';
            value = obj.read()
            # value = [random.uniform(50.0,99.7),random.uniform(13.5,33.5)]
            tools.append_temp_to_data_dxnry(data_dxnry,value[1],obj.toISO8601(datetime.datetime.now()))
            tools.append_umid_to_data_dxnry(data_dxnry,value[0],obj.toISO8601(datetime.datetime.now()))
            obj.check_dispatch(value,snap_dxnry)
        if (obj.active[0] == False): obj.stat[0] = 'INACTIVE';
        if (obj.active[1] == False): obj.stat[1] = 'INACTIVE';

# AUX ##########################################################################

    def toDelta(obj,t):
        return datetime.timedelta(0,t.hour*3600 + t.minute*60 + t.second)

    def toISO8601(obj,t):
        return datetime.datetime.strftime(t,'%Y-%m-%d')+'T'+datetime.datetime.strftime(t,'%H:%M')+'Z'
