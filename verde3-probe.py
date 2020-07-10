import probe_config
import probe_operation
import probe_connection
#
import datetime, time

connected = probe_connection.check_connection(); init = True

while(True):
    if (connected == True):
        if (init == True):
            current_config_date = probe_config.get_config_date()
            snsrs, reles = probe_config.new_probe_config([5,6,26],[12,16,20,21])
            snapshot = probe_config.new_snapshot()
            init = False

        probe_operation.verify_snsrs_operation(snsrs,snapshot)

        probe_operation.verify_relay_operation(reles)

        print('SENS. TEMPERATURE','|',datetime.datetime.strftime(snsrs[0].dt,"%H:%M:%S"),'|',snsrs[0].active)
        print('SENS. HUMIDITY   ','|',datetime.datetime.strftime(snsrs[1].dt,"%H:%M:%S"),'|',snsrs[1].active)
        print('SENS. LUMINOSITY ','|',datetime.datetime.strftime(snsrs[2].dt,"%H:%M:%S"),'|',snsrs[2].active)
        #
        print(reles[0].name,'|','ACTIV.:',reles[0].is_active,'|','PERIODIC:',reles[0].is_periodic,'|','STATUS:',reles[0].stat,'|','TIME ACT.:',datetime.datetime.strftime(reles[0].dt_act,"%H:%M:%S"),'|','TIME INACT.:',datetime.datetime.strftime(reles[0].dt_inact,"%H:%M:%S"))
        print(reles[1].name,'|','ACTIV.:',reles[1].is_active,'|','PERIODIC:',reles[1].is_periodic,'|','STATUS:',reles[1].stat,'|','TIME ACT.:',datetime.datetime.strftime(reles[1].dt_act,"%H:%M:%S"),'|','TIME INACT.:',datetime.datetime.strftime(reles[1].dt_inact,"%H:%M:%S"))
        print(reles[2].name,'|','ACTIV.:',reles[2].is_active,'|','PERIODIC:',reles[2].is_periodic,'|','STATUS:',reles[2].stat,'|','TIME ACT.:',datetime.datetime.strftime(reles[2].dt_act,"%H:%M:%S"),'|','TIME INACT.:',datetime.datetime.strftime(reles[2].dt_inact,"%H:%M:%S"))
        print(reles[3].name,'   |','ACTIV.:',reles[3].is_active,'|','PERIODIC:',reles[3].is_periodic,'|','STATUS:',reles[3].stat,'|','TIME ACT.:',datetime.datetime.strftime(reles[3].dt_act,"%H:%M:%S"),'|','TIME INACT.:',datetime.datetime.strftime(reles[3].dt_inact,"%H:%M:%S"))
        #
        print('SNAPSHOT STATUS:',snapshot.stat)
        print('DATA TEMPERATURE:',snapshot.value[0],'Timestamp:',snapshot.date[0])
        print('DATA HUMIDITY   :',snapshot.value[1],'Timestamp:',snapshot.date[1])
        print('DATA LUX        :',snapshot.value[2],'Timestamp:',snapshot.date[2])
        #
        print(datetime.datetime.strftime(datetime.datetime.now(),"%H:%M:%S"))
        print('\n')

        if (probe_operation.dispatch_snapshot(snapshot) == True):
            snapshot = probe_config.new_snapshot()

        if (probe_config.verify_probe_update(current_config_date) == True):
            current_config_date = probe_config.get_config_date()
            snsrs, reles = probe_config.update_probe_config(snsrs,reles)

    #CHECK CONNECTION
    if (connected == False):
        while(connected == False):
            connected = probe_connection.check_connection()
