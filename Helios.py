#!/usr/bin/python
from time import sleep
from heliospy import *
import paho.mqtt.publish as mqtt
import json

data_dict = {}
helios = HeliosBase()
helios.connect()

while helios._is_connected:

    for var in CONST_MAP_VARIABLES_TO_ID.keys():
#        print("{0} = {1}".format(var,helios.readValue(var)))
        data_dict[var]=str(helios.readValue(var))

#    mqtt.single("helios",json.dumps(data_dict))
    mqtt.single("helios", json.dumps(data_dict), retain=False, qos=2, keepalive=120, client_id="helios")
    time.sleep(60)

#except Exception as e:
#    print("Exception: {0}".format(e))
#    return 1
#finally:
#    if helios:
#        helios.disconnect()

#while True:
    #do some serial sending here
