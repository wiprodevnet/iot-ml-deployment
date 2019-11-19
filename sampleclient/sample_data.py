"""
This is for payload data and IP configuration.
"""
#Configure the IOX Webserver IP and port.
FOG_APP_IP = '127.0.0.1:5000'
#FOG_APP_IP = '10.10.20.51:40000'

#Select appropriate payload data as per ML model deployed

#Payload for multivariant model

#Payload for univariant model i.e., only hour
PAYLOAD = {'hour': 0}

#Payload for multivariant model i.e., categorical vlaues for hour_
#PAYLOAD = {'hour_1':0, 'hour_2':0, 'hour_3':0, 'hour_4':0, 'hour_5':0, 'hour_6':0, 'hour_7':1,
#       'hour_8':0, 'hour_9':0, 'hour_10':0, 'hour_11':0, 'hour_12':0, 'hour_13':0,
#       'hour_14':0, 'hour_15':0, 'hour_16':0, 'hour_17':0, 'hour_18':0, 'hour_19':0,
#       'hour_20':0, 'hour_21':0, 'hour_22':0, 'hour_23':0}
             
