from ctypes import c_uint16
from ctypes import c_uint32
from ctypes import c_uint64
from ctypes import CDLL
from ctypes import Structure
from ctypes import cast
from ctypes import POINTER
from ctypes import pointer
from ctypes import c_float
from objects import c_TrafficLight
from objects import c_RoadUser

class Message:
        
    def __init__(self, cam_idx, t_stamp_ms):
        self.cam_idx=c_uint32(cam_idx).value
        self.t_stamp_ms=c_uint64(t_stamp_ms).value

class MasaMessage(Message):
    
    def __init__ (self, cam_idx, t_stamp_ms, num_objects, objects, lights):
        super().__init__(cam_idx, t_stamp_ms)
        self.num_objects = c_uint16(num_objects).value
        self.objects = objects
        self.lights = lights
        
    def printMessage (self):
        print(self.cam_idx)
        print(self.t_stamp_ms)
        print(self.num_objects)
        
    def serializeMessage (self):
        all_param = []
        all_param.append(self.cam_idx)
        all_param.append(self.t_stamp_ms)
        all_param.append(self.num_objects)
        for o in self.objects:
            for i in o.serializeObject():
                all_param.append(i)
        all_param.append(len(self.lights))
        for l in self.lights:
            for i in l.serializeObject():
                all_param.append(i)
        return all_param
    
    def send(self):
        c_lib = CDLL("/home/vlad/Tirocinio/Altro/libreria.lib") #insert library path
        
class c_MasaMessage(Structure):
    _fields_ = [
            ("cam_idx", c_uint32),
            ("t_stamp_ms", c_uint64),
            ("num_objects", c_uint16),
            ("objects", POINTER(c_RoadUser)),
            ("lights", POINTER(c_TrafficLight)),
            ]        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        