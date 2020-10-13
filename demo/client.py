#Importing MasaProtocol from directory
import sys
sys.path.insert(1, '../python')
from MasaProtocol import *

#Creating MasaMessage
objects = []
objects.append(RoadUser(0.5, 0.6, 100, 70, "C_person"))
objects.append(RoadUser(0.7, 2.6, 120, 60, "C_bycicle"))
objects.append(RoadUser(1.4, 0.2, 400, 90, "C_car"))
objects.append(RoadUser(1.4, 0.2, 400, 90, "C_car"))
objects.append(RoadUser(1.4, 0.2, 400, 90, "C_car"))
lights = []
lights.append(TrafficLight(0.4, 0.6, 99, "L_green", 7))
lights.append(TrafficLight(3.5, 0.5, 54, "L_yellow", 8))
message = MasaMessage(20, 40, 5, objects, lights)

#Sending the message at given IP and PORT
message.send("127.0.0.1", 8888)

#Otherwise you can do:
#MasaMessage.send(message, "127.0.0.1", 8888)
