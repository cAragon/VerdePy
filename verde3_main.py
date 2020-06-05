# importar bibliotecas
import datetime, time
import verde3_tools as tools, verde3_disp as display

# GET RASPBERRY PI SERIAL
pi = {"_id": tools.get_pi_serial()}

# GET BEAR TOKEN FROM VERDE3 API
cod, bear_token = tools.get_bear_token('https://auth-verdeaocubo.herokuapp.com/tokens/probe/',pi)
print(bear_token)
time.sleep(10)
# SET AUTHENTICATION HEADER TO VERDE3 API
headers = {"Authorization": ('Bearer '+bear_token['token'])}

# GET PI CONFIG DATE
config_date = tools.get_config_date('https://api-verdeaocubo.herokuapp.com/probes/me/config/date',headers)

# GET PI CONFIG JSON
cod, probe_config = tools.get_probe_config('https://api-verdeaocubo.herokuapp.com/probes/me/config',headers)

# SET PROBE OBJECTS
ldr, dht, dsp = tools.set_probe_config(probe_config)

# SET DATA BACKLOG
data_dxnry = tools.set_data_dxnry()

# SET DATA SNAPSHOT
snap_dxnry = tools.set_snapshot_dxnry()

# RUN PROBE OPERATION
display.header()
while (True):

    # CHECK SENSOR MODULE OPERATION
    ldr.check_op(data_dxnry,snap_dxnry)
    dht.check_op(data_dxnry,snap_dxnry)

    # CHECK CONTROL MODULE OPERATION
    for i in range(0,4): dsp[i].check_op();

    #print("\033c")
    # display.snsr_module(ldr,dht)
    # display.ctrl_module(dsp)

    display.dxnry(datetime.datetime.strftime(datetime.datetime.now(),'%d-%m-%Y %H:%M:%S'),
                    data_dxnry['Dados de Luminosidade'][-1]['Valor']                     ,
                    data_dxnry['Dados de Temperatura'][-1]['Valor']                      ,
                    data_dxnry['Dados de Umidade'][-1]['Valor']                          ,
                    snap_dxnry['dispatch']                                               )

    # CHECK SNAPSHOT DISPATCH
    if (snap_dxnry['dispatch'] == True):
        cod = tools.dispatch_snapshot('https://api-verdeaocubo.herokuapp.com/probes/me/snapshots', snap_dxnry, headers)
        #print(cod)
        snap_dxnry = tools.set_snapshot_dxnry()

    # CHECK USER UPDATES
    # if (tools.get_config_date('https://api-verdeaocubo.herokuapp.com/probes/me/config/date',headers).time() >= config_date.time()):
        # GET PI CONFIG JSON
        # cod, probe_config = tools.get_probe_config('https://api-verdeaocubo.herokuapp.com/probes/me/config',headers)
        # PROBE OBJECTS
        # ldr, dht, dsp = tools.set_probe_config(probe_config)

    time.sleep(1)
