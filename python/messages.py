from ctypes import cast, c_char, CDLL, c_float, c_int, c_uint8, c_uint16, c_uint32, c_uint64, POINTER, Structure
from objects import *


class Message():
    """
    Primitive message class.
    This is the python version of the "message" in C.
    All future messages based of this class must extend it.
    """
    def __init__(self, cam_idx, t_stamp_ms):
        self.cam_idx = c_uint32(cam_idx).value
        self.t_stamp_ms = c_uint64(t_stamp_ms).value

    def send(self, cam_idx, t_stamp_ms):
        #TODO Implement the standard message class
        pass

    def __str__(self):
        return f"Message with: cam_idx={self.cam_idx}, t_stamp_ms={self.t_stamp_ms}."


class MasaMessage(Message):
    """
    This is the python version of the "MasaMessage" C class.
    """
    def __init__ (self, cam_idx, t_stamp_ms, num_objects, objects, lights):
        #Initializing superclass Message
        Message.__init__(self, cam_idx, t_stamp_ms)
        #Finishing with MasaMessage attributes
        self.num_objects = c_uint16(num_objects).value
        self.num_lights = c_uint16(len(lights)).value
        self.objects = objects
        self.lights = lights

    def send(self, ip, port):
        #Initializing C lib functions
        lib=CDLL("../masa_c_lib/masa_python_c_lib.lib")
        lib.create_MasaMessage.argtypes = [c_uint32, c_uint64, c_uint16, c_uint16, POINTER(c_RoadUser), POINTER(c_TrafficLight)]
        lib.create_MasaMessage.restypes = [POINTER(c_MasaMessage)]
        lib.send_MasaMessage.argtypes = [POINTER(c_MasaMessage), c_int, POINTER(c_char)]
        lib.send_MasaMessage.restypes = [c_int]
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
        return lib.send_MasaMessage(message, c_int(port), ip.encode("utf-8"))

    def receive(raw_data):
        #Initializing C lib functions
        lib=CDLL("../masa_c_lib/masa_python_c_lib.lib")
        lib.receive_MasaMessage.argtypes = [POINTER(c_char), c_uint32]
        lib.receive_MasaMessage.restypes = [POINTER(c_MasaMessage)]
        #Preparing the data for the c lib
        data_len = len(raw_data)
        raw_data = cast(raw_data, POINTER(c_char))
        #Calling c lib for data parsing
        message = lib.receive_MasaMessage(raw_data, data_len)
        message = cast(message, POINTER(c_MasaMessage))
        #Converting objects and lights
        objects = []
        for i in range(message[0].num_objects):
            o = RoadUser(message[0].objects[i].latitude, message[0].objects[i].longitude, message[0].objects[i].speed, message[0].objects[i].orientation, 		Categories.name(message[0].objects[i].category))
            objects.append(o)
        lights = []
        for i in range(message[0].num_lights):
            l = TrafficLight(message[0].lights[i].latitude, message[0].lights[i].longitude, message[0].lights[i].orientation, LightStatus.name(message[0].lights[i].status), message[0].lights[i].time_to_change)
            lights.append(l)
        #Returning the complete message
        return MasaMessage(message[0].cam_idx, message[0].t_stamp_ms, message[0].num_objects, objects, lights)

    def __str__(self):
        return f"MasaMessage with: cam_idx={self.cam_idx}, t_stamp_ms={self.t_stamp_ms}, num_objects={self.num_objects}, num_lights={self.num_lights}."


class c_MasaMessage(Structure):
    """
    This is the mid version of a python MasaMessage.
    In normal conditions you are not supposed to use this object!
    """
    _fields_ = [
            ("cam_idx", c_uint32),
            ("t_stamp_ms", c_uint64),
            ("num_objects", c_uint16),
            ("num_lights", c_uint16),
            ("objects", POINTER(c_RoadUser)),
            ("lights", POINTER(c_TrafficLight))
            ]


class c_Message(Structure):
    """
    This is the mid version of a python Message.
    In normal conditions you are not supposed to use this object!
    """
    _fields_ = [
            ("cam_idx", c_uint32),
            ("t_stamp_ms", c_uint64)
            ]
