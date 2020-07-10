import ops_time, ops_api

def init(reles):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in range(0,4): reles[i].init();

def add_to_snapshot(snapshot,value,i):
    snapshot.set_stat(True)
    snapshot.set_value(value,i)
    snapshot.set_date(ops_time.now_UTM0_toISO8601(),i)

def dispatch_snapshot(snapshot):
    if (snapshot.get_stat() == True):
        code =  ops_api.send_snapshot(snapshot.content({}))
        if (code == 201):
            return True
    else:
        return False

def verify_snsrs_operation(snsrs,snapshot):
    for i in range (0,3):
        if (snsrs[i].get_active() == True):
            if (snsrs[i].get_stat() == 'INACTIVE'): snsrs[i].set_stat('ACTIVE');
            value = snsrs[i].read_snsr()
            if (ops_time.verify_snsr_dt_(snsrs[i].get_read(),snsrs[i].get_dt()) == True):
                add_to_snapshot(snapshot,value,i)
                new = ops_time.sum_dt(snsrs[i].get_read(),snsrs[i].get_dt())
                snsrs[i].set_read(new)
        if (snsrs[i].get_active() == False):
            if (snsrs[i].get_stat() == 'ACTIVE'): snsrs[i].set_stat('INACTIVE');

def verify_relay_operation(reles):
    for i in range(0,4):
        if (reles[i].get_is_active() == True):
            if (reles[i].get_stat() == 'DEACTIVATED'):
                reles[i].set_stat('ACTIVE')
                reles[i].activate()
            if (reles[i].get_is_periodic() == True):
                if (reles[i].get_stat() == 'ACTIVE'):
                    if(ops_time.verify_rele_dt(ops_time.deactivation_dt(reles[i].get_next_act(),reles[i].get_dt_act())) == True):
                        reles[i].deactivate()
                        reles[i].set_stat('INACTIVE')
                if (reles[i].get_stat() == 'INACTIVE'):
                    if(ops_time.verify_rele_dt(ops_time.reactivation_dt(reles[i].get_next_act(),reles[i].get_dt_act(),reles[i].get_dt_inact())) == True):
                        reles[i].activate()
                        reles[i].set_stat('ACTIVE')
                        reles[i].set_next_act(ops_time.reactivation_dt(reles[i].get_next_act(),reles[i].get_dt_act(),reles[i].get_dt_inact()))
        if (reles[i].get_is_active() == False):
            reles[i].deactivate()
            reles[i].set_stat('DEACTIVATED')
