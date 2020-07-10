import ops_time

class snapshot:

# CONSTRUTOR ###################################################################

    def __init__(obj,stat):
        obj.stat = stat
        obj.value = [-9.99,-9.99,-9.99]
        obj.date  = [ops_time.now_UTM0_toISO8601(),
                     ops_time.now_UTM0_toISO8601(),
                     ops_time.now_UTM0_toISO8601()]

# METHODS ######################################################################

    def get_stat(obj):
        return obj.stat

    def get_value(obj,i):
        return obj.value[i]

    def get_date(obj,i):
        return obj.date[i]

    def set_stat(obj,stat):
        obj.stat = stat

    def set_value(obj,value,i):
        obj.value[i] = value

    def set_date(obj,date,i):
        obj.date[i] = date

    # Dá pra fazer um void aqui
    def content(obj,dxnry):
        dxnry['snapshot'] = {'content': [
             {'type': 'temp' , 'data': obj.value[0] , 'timestamp': obj.date[0]},
             {'type': 'umid' , 'data': obj.value[1] , 'timestamp': obj.date[1]},
             {'type': 'light', 'data': obj.value[2] , 'timestamp': obj.date[2]}]}
        return dxnry
