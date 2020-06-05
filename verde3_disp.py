import datetime

def header():
    print ('------------------------------------------------------------------'   +
           '\n                                                                   '+
           '\n SISTEMA VERDE AO CUBO                                             '+
           '\n                                                                   '+
           '\n-------------------------------------------------------------------'+
           '\n        Date         | RCTime s | Temp. *C | Umid. % |  DISPATCHED  ')

def dash_line():
    print('--------------------------------------------------------------------------------------------------------------')

def snsr_module(obj_ldr,obj_dht):
    print('Sensor de Luminosidade'+' | TYPE: LDR'+' | dt: '+datetime.datetime.strftime(obj_ldr.dt,'%H:%M:%S') +' | STATUS: '+obj_ldr.stat)
    print('Sensor de Temperatura '+' | TYPE: DHT'+' | dt: '+datetime.datetime.strftime(obj_dht.dt[0],'%H:%M:%S')+' | STATUS: '+obj_dht.stat[0])
    print('Sensor de Umidade     '+' | TYPE: DHT'+' | dt: '+datetime.datetime.strftime(obj_dht.dt[1],'%H:%M:%S')+' | STATUS: '+obj_dht.stat[1])
    dash_line()

def ctrl_module(obj_disp):
    for i in range(0,4):
        print(obj_disp[i].name+' | PERIODIC MODE: '+str(obj_disp[i].is_periodic)+' | TIME ACTIVE: '+datetime.datetime.strftime(obj_disp[i].dt_act,'%H:%M:%S')+' | TIME INACTIVE: '+datetime.datetime.strftime(obj_disp[i].dt_inact,'%H:%M:%S')+' | STATUS: '+obj_disp[i].stat)
    dash_line()

def dxnry(t,lux,temp,umid,stat):
    print(t,' |  {0:0.2f}'.format(lux),' |  {0:0.2f}'.format(temp),'  |  {0:0.2f}'.format(umid),' |   ',stat)
