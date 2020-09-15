from ctypes import *
from objects import c_RoadUser, c_TrafficLight
from messages import c_MasaMessage


lib=CDLL("./masa_c_lib/masa_python_c_lib.lib")
lib.initialize_message.argtypes = [c_uint16, c_uint16]
lib.initialize_message.restypes = [POINTER(c_MasaMessage)]
lib.prepare_message.argtypes = []


res = lib.initialize_message(c_uint16(3), c_uint16(3))
res = cast(res, POINTER(c_MasaMessage))

print(res[0].num_lights)




"""
class sotto_messaggio(Structure):
    _fields_ = [("x", c_int),("y", c_int)]

class messaggio(Structure):
	_fields_ = [("a",c_int),("b",c_int),("c",c_float),("sm", sotto_messaggio)]
	
	
lib.inizializza_messaggio.argtypes = [c_int]
lib.inizializza_messaggio.restypes = [POINTER(messaggio)]
m = lib.inizializza_messaggio(c_int(2))

m = cast(m,POINTER(messaggio))
m[1].a = c_int(9)
m[1].b = c_int(7)
m[1].c = c_float(9.00)
m[1].sm.x = c_int(99)
m[1].sm.y = c_int(909)


for mes in range(2):
    print(m[mes].a)
    print(m[mes].b)
    print(m[mes].c)
    print(m[mes].sm.x)
    print(m[mes].sm.y)



"""