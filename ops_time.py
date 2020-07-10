import datetime

def toSeconds(t):
    return datetime.timedelta(0,t.hour*3600 + t.minute*60 + t.second)

def toISO8601(t):
    return datetime.datetime.strftime(t,'%Y-%m-%d')+'T'+datetime.datetime.strftime(t,'%H:%M:%S')+'Z'

def now_UTM0_toISO8601():
    return toISO8601(datetime.datetime.now()+datetime.timedelta(hours=3))

def verify_snsr_dt_(read,dt):
    if (datetime.datetime.now().time() >= sum_dt(read,dt).time()):
        return True
    else:
        return False

def verify_rele_dt(dt):
    if (datetime.datetime.now().time() >= dt.time()):
        return True
    else:
        return False

def sum_dt(read,dt):
    return read + toSeconds(dt)

def diff_dt(dt):
    return datetime.datetime.now() - toSeconds(dt)

def deactivation_dt(next_act,dt_act):
    return next_act+toSeconds(dt_act.time())

def reactivation_dt(next_act,dt_act,dt_inact):
    return next_act+toSeconds(dt_act.time())+toSeconds(dt_inact.time())

def format_dt(dt):
    return datetime.datetime.strptime(dt  , '%H:%M:%S')

def new_dt():
    return datetime.datetime.now()
