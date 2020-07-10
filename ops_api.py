import requests
import datetime
import dateutil.parser
import ops_rasp

def new_pi_id():

    return {"_id": ops_rasp.get_pi_serial()}

def get_bearer_token(pi_id):

    request_bearer_token = requests.post('https://auth-verdeaocubo.herokuapp.com/tokens/probe/',json=pi_id)

    return request_bearer_token.json()

def set_headers(pi_serial):

    pi_id = new_pi_id()

    bearer_token = get_bearer_token(pi_id)

    return {"Authorization": ('Bearer '+bearer_token['token'])}

def request_probe_config():

    headers = set_headers(ops_rasp.get_pi_serial())

    request_config = requests.get('https://api-verdeaocubo.herokuapp.com/probes/me/config',headers=headers)

    return request_config.json()

def request_config_date():

    headers = set_headers(ops_rasp.get_pi_serial())

    request = requests.get('https://api-verdeaocubo.herokuapp.com/probes/me/config/date',headers=headers)

    date = dateutil.parser.parse(request.json()['date'])

    date = datetime.datetime(date.year,date.month,date.day,date.hour,date.minute,date.second)

    return date

def send_snapshot(snap_dxnry):

    headers = set_headers(ops_rasp.get_pi_serial())

    r = requests.post('https://api-verdeaocubo.herokuapp.com/probes/me/snapshots',headers=headers,json=snap_dxnry['snapshot'])

    return r.status_code
