
import dht
import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Conversions between binary data and various encodings
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import random                 # Random number generator
from machine import Pin       # Define pin
from secrets import secrets

# BEGIN SETTINGSS
# These need to be change to suit your environment


# Wireless network
WIFI_SSID = secrets["ssid"]
WIFI_PASS = secrets["password"] # No this is not our regular password. :)

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "" #Your Username here
AIO_KEY =  "" #Your AIO Key here
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_RANDOMS_FEED = "" #Adress for temp, could not change the name randoms for some reason
AIO_HUMIDITY_FEED = "" # adress for humidity
 
# END SETTINGS

# FUNCTIONS

tempSensor = dht.DHT11(Pin(27))

#Send temperature data from sensor
def send_temperature(temperature):
    feed = "Braver_Parrot/feeds/random"  
    msg = str(temperature)
    print("Publishing temperature:", temperature)
    client.publish(topic=feed, msg=msg)

#Send the humidtu data from sensor
def sen_humidity(humidity):
    feed = "Braver_Parrot/feeds/humidity"
    msg = str(humidity)
    print("Publishing humidty:",humidity)
    client.publish(topic=feed,msg=msg)    
    

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

# Subscribed messages will be delivered to this callback
client.connect()

try:                      # Code between try: and finally: may cause an error
                          # so ensure the client disconnects the server if
                          # that happens.
    while 1:              # Repeat this loop forever
        client.check_msg()# Action a message if one is received. Non-blocking.
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
      
        # Skicka temperaturdata till Adafruit IO
        send_temperature(temperature)
        sen_humidity(humidity)

        time.sleep(20)
        
finally:                  # If an exception is thrown ...
    client.disconnect()   # ... disconnect the client and clean up.
    client = None
    print("Disconnected from Adafruit IO.")
