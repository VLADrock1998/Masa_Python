from ctypes import c_uint8
from ctypes import c_uint16
from ctypes import c_uint32
from ctypes import c_uint64
from ctypes import c_char
from ctypes import CDLL
from ctypes import Structure
from ctypes import cast
from ctypes import POINTER
from ctypes import c_float
from ctypes import c_int
from objects import c_TrafficLight
from objects import c_RoadUser


class MasaMessage():
    
    def __init__ (self, cam_idx, t_stamp_ms, num_objects, objects, lights):
        self.cam_idx = c_uint32(cam_idx).value
        self.t_stamp_ms = c_uint64(t_stamp_ms).value
        self.num_objects = c_uint16(num_objects).value
        self.num_lights = c_uint16(len(lights)).value
        self.objects = objects
        self.lights = lights

    def send(self, port, ip):
        #Initializing C lib functions
        lib=CDLL("./masa_c_lib/masa_python_c_lib.lib")
        lib.create_MasaMessage.argtypes = [c_uint32, c_uint64, c_uint16, c_uint16, POINTER(c_RoadUser), POINTER(c_TrafficLight)]
        lib.create_MasaMessage.restypes = [POINTER(c_MasaMessage)]
        lib.send_message.argtypes = [POINTER(c_MasaMessage), c_int, POINTER(c_char)]
        lib.send_message.restypes = [c_int]
        lib.create_RoadUser.argtypes = [c_uint16]
        lib.create_RoadUser.restypes = [POINTER(c_RoadUser)]
        lib.create_TrafficLight.argtypes = [c_uint16]
        lib.create_TrafficLight.restypes = [POINTER(c_TrafficLight)]
        lib.initialize_RoadUser.argtypes = [POINTER(c_RoadUser), c_float, c_float, c_uint8, c_uint16, c_uint8]
        lib.initialize_RoadUser.restypes = [POINTER(c_RoadUser)]
        lib.initialize_TrafficLight.argtypes = [POINTER(c_TrafficLight), c_float, c_float, c_uint8, c_uint8, c_uint8]
        lib.initialize_TrafficLight.restypes = [POINTER(c_TrafficLight)]
        #Converting objects and lights to C structs
        objects = lib.create_RoadUser(self.num_objects)
        objects = cast(objects, POINTER(c_RoadUser))
        lights = lib.create_TrafficLight(self.num_lights)
        lights = cast(lights, POINTER(c_TrafficLight))
        for i in range(self.num_objects):
            lib.initialize_RoadUser(objects[i], self.objects[i].latitude, self.objects[i].longitude, self.objects[i].speed, self.objects[i].orientation, self.objects[i].category.convert())
        for i in range(self.num_lights):
            lib.initialize_TrafficLight(lights[i], self.lights[i].latitude, self.lights[i].longitude, self.lights[i].orientation, self.lights[i].status.convert(), self.lights[i].time_to_change)
        #Creating the message to send
        message = lib.create_MasaMessage(self.cam_idx, self.t_stamp_ms, self.num_objects, self.num_lights, objects, lights)
        message = cast(message, POINTER(c_MasaMessage))
        #Sending the message, if error -> Return !=0
        return lib.send_message(message, c_int(port), ip.encode("utf-8"))
        
        
class c_MasaMessage(Structure):
    _fields_ = [
            ("cam_idx", c_uint32),
            ("t_stamp_ms", c_uint64),
            ("num_objects", c_uint16),
            ("num_lights", c_uint16),
            ("objects", POINTER(c_RoadUser)),
            ("lights", POINTER(c_TrafficLight)),
            ]        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        