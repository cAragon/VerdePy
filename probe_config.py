import ops_api, ops_time

def get_config_date():
    return ops_api.request_config_date()

def new_dxnry():
    return []

def new_snapshot():
    from snapshot import snapshot
    return snapshot(False)

def init_snsrs_objs(dxnry,probe_config,pins):
    from dht import dht
    from ldr import ldr
    for i in range(0,3):
        if (i < 2):
            dxnry.append(dht(probe_config['sensors'][i]['type'],
                             probe_config['sensors'][i]['dt'],
                             pins[i],
                             probe_config['sensors'][i]['is_active']))
        if (i == 2):
            dxnry.append(ldr(probe_config['sensors'][i]['type'],
                             probe_config['sensors'][i]['dt'],
                             pins[i],
                             probe_config['sensors'][i]['is_active']))
    return dxnry

def init_rele_objs(dxnry,probe_config,pins):
    from rele import rele
    for i in range(0,4):
        dxnry.append(rele(probe_config['devices'][i]['name'],
                          probe_config['devices'][i]['is_active'],
                          probe_config['devices'][i]['is_periodic'],
                          probe_config['devices'][i]['act_time'],
                          probe_config['devices'][i]['inact_time'],
                          pins[i]))
    return dxnry

def new_probe_config(snsr_pins,rele_pins):
    probe_config = ops_api.request_probe_config()
    return init_snsrs_objs(new_dxnry(),probe_config,snsr_pins), init_rele_objs(new_dxnry(),probe_config,rele_pins)

def verify_probe_update(current_config_date):
    if (current_config_date.time() < get_config_date().time()):
        return True
    else:
        return False

def update_snsrs_objs(snsrs,probe_config):
    for i in range(0,3):
        snsrs[i].set_dt(ops_time.format_dt(probe_config['sensors'][i]['dt']))
        snsrs[i].set_active(probe_config['sensors'][i]['is_active'])
    return snsrs

def update_reles_objs(reles,probe_config):
    for i in range(0,4):
        reles[i].set_name(probe_config['devices'][i]['name'])
        reles[i].set_is_active(probe_config['devices'][i]['is_active'])
        reles[i].set_is_periodic(probe_config['devices'][i]['is_periodic'])
        reles[i].set_dt_act(ops_time.format_dt(probe_config['devices'][i]['act_time']))
        reles[i].set_dt_inact(ops_time.format_dt(probe_config['devices'][i]['inact_time']))
        reles[i].set_next_act(ops_time.new_dt())
    return reles

def update_probe_config(snsrs,reles):
    probe_config = ops_api.request_probe_config()
    return update_snsrs_objs(snsrs,probe_config), update_reles_objs(reles,probe_config)
