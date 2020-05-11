from ctypes import c_uint16
from ctypes import c_uint32
from ctypes import c_uint64
from objects import Categories
from objects import RoadUser

class Message:
        
    def __init__(self, cam_idx, t_stamp_ms):
        self.cam_idx=c_uint32(cam_idx).value
        self.t_stamp_ms=c_uint64(t_stamp_ms).value

class MasaMessage(Message):

	def __init__(self, num_objects, objects, lights):
		self.num_objects = c_uint16(num_objects).value

	def printMessage (self):
		print(self.cam_idx)
		print(self.t_stamp_ms)
		print(self.num_objects)