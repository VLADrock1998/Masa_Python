from messages import MasaMessage
from objects import RoadUser, TrafficLight

objects = []
objects.append(RoadUser(0.5, 0.6, 100, 70, "C_person"))
objects.append(RoadUser(0.7, 2.6, 120, 60, "C_bycicle"))
objects.append(RoadUser(1.4, 0.2, 400, 90, "C_car"))
lights = []
lights.append(TrafficLight(0.4, 0.6, 99, "L_green", 7))
lights.append(TrafficLight(3.5, 0.5, 54, "L_yellow", 8))
lights.append(TrafficLight(2.9, 0.2, 70, "L_red", 10))
message = MasaMessage(20, 40, 3, objects, lights)

message.send(8891, "127.0.0.1")