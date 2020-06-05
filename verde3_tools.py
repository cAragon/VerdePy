# LIBRARIES
import json
import requests
import datetime
import dateutil.parser

# PI TOOLS
def get_pi_serial():
  piserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        piserial = line[10:26]
    f.close()
  except:
    piserial = "000000000e2e9562"
  return piserial

# API TOOLS
def get_bear_token(url,pi_serial):
    request = requests.get(url,json=pi_serial)
    return request.status_code, request.json()

def get_probe_config(url,headers):
    request = requests.get(url,headers=headers)
    return request.status_code, request.json()

def get_config_date(url,headers):
    request = requests.get(url,headers=headers)
    date = dateutil.parser.parse(request.json()['date'])
    date = datetime.datetime(date.year,date.month,date.day,date.hour,date.minute,date.second)
    return date

# PROBE TOOLS
def set_probe_config(probe_config):
    from DHT  import DHT
    from LDR  import LDR
    from RELE import RELE

    ldr = LDR('Sensor LDR',
              probe_config['sensors'][2]['dt'],
              probe_config['sensors'][2]['is_active'])
    dht = DHT('Sensor DHT',
              probe_config['sensors'][0]['dt'],
              probe_config['sensors'][1]['dt'],
              probe_config['sensors'][0]['is_active'],
              probe_config['sensors'][1]['is_active'])

    dsp = []; pins = [12,16,20,21];

    for i in range(0,4):
        dsp.append(RELE(probe_config['devices'][i]['name'],
                        probe_config['devices'][i]['is_active'],
                        probe_config['devices'][i]['is_periodic'],
                        probe_config['devices'][i]['act_time'],
                        probe_config['devices'][i]['inact_time'],
                        pins[i]))
    del pins
    return ldr, dht, dsp

# DATA TOOLS
def set_data_dxnry ():
    data = {}
    data['Dados de Temperatura' ] = []
    data['Dados de Umidade'     ] = []
    data['Dados de Luminosidade'] = []
    return data

def append_temp_to_data_dxnry(dxnry,value,date):
    dxnry['Dados de Temperatura'].append({
    'Valor'               : value  ,
    'Data de Amostragem'  : date   ,
    })

def append_umid_to_data_dxnry(dxnry,value,date):
    dxnry['Dados de Umidade'].append({
    'Valor'               : value  ,
    'Data de Amostragem'  : date   ,
    })

def append_lux_to_data_dxnry(dxnry,value,date):
    dxnry['Dados de Luminosidade'].append({
    'Valor'               : value  ,
    'Data de Amostragem'  : date   ,
    })

# SNAPSHOT TOOLS
def set_snapshot_dxnry():
    data = {}
    data['dispatch'] = False
    data['snapshot'] = {'content': [
        {'type': 'light', 'data': 0.0 , 'timestamp': '1900-01-01T00:00Z'},
        {'type': 'temp' , 'data': 0.0 , 'timestamp': '1900-01-01T00:00Z'},
        {'type': 'umid' , 'data': 0.0 , 'timestamp': '1900-01-01T00:00Z'},
    ]}
    return data

def append_to_snapshot(snap_dxnry,i,value,date):
    snap_dxnry['snapshot']['content'][i]['data'] = value
    snap_dxnry['snapshot']['content'][i]['timestamp'] = date

def dispatch_snapshot(url,snap_dxnry,headers):
    r = requests.post(url,headers=headers,json=snap_dxnry['snapshot'])
    return r.status_code
