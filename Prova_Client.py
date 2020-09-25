from messages import MasaMessage
from objects import RoadUser, TrafficLight

#Creazione MasaMessage
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

#Invio passando ip e porta
message.send("127.0.0.1", 8891)

#In alternativa, per questioni di coerenza con il MasaMessage.receive():
#MasaMessage.send(message, "127.0.0.1", 8891)