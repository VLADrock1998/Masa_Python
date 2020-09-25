from ctypes import c_uint8
from ctypes import c_uint16
from ctypes import c_float
from ctypes import Structure

class Categories:

    categories_list={
        "C_person":c_uint8(14).value,
        "C_bycicle":c_uint8(1).value,
        "C_car":c_uint8(6).value,
        "C_motorbike":c_uint8(13).value,
            "C_bus":c_uint8(5).value,
            "C_marelli1":c_uint8(20).value,
            "C_marelli2":c_uint8(21).value,
            "C_quattroporte":c_uint8(30).value,
            "C_levante":c_uint8(31).value,
            "C_rover":c_uint8(40).value}

    def __init__(self, category):
        if category not in Categories.categories_list:
            print("ERRORE!!!!")
            return
        self.category=c_uint8(Categories.categories_list[category])

    def convert(self):
        return self.category

    def name(value):
        for k,v in Categories.categories_list.items():
            if v == value:
                return k

    def printCategories ():
        for c in Categories.categories_list:
            print(c," ",Categories.categories_list.get(c))

    def __str__(self):
        return str(self.category.value)

class LightStatus:

    statuses_list={
            "L_green":c_uint8(1).value,
            "L_yellow":c_uint8(2).value,
            "L_red":c_uint8(3).value}

    def __init__(self, status):
        if status not in LightStatus.statuses_list:
            print("ERRORE!!!!")
            return
        self.status=c_uint8(LightStatus.statuses_list[status])

    def convert(self):
        return self.status

    def name(value):
        for k,v in LightStatus.statuses_list.items():
            if v == value:
                return k

    def printStatuses():
        for s in LightStatus.statuses_list:
            print(s," ",LightStatus.statuses_list.get(s))

    def __str__(self):
        return str(self.status.value)

class TrafficLight:

    def __init__(self, latitude, longitude, orientation, status, time_to_change):
        self.status=LightStatus(status)
        self.latitude=c_float(latitude).value
        self.longitude=c_float(longitude).value
        self.orientation=c_uint8(orientation).value
        self.time_to_change=c_uint8(time_to_change).value

    def __str__(self):
        return f"TrafficLight with: latitude={self.latitude}, longitude={self.longitude}, orientation={self.orientation}, status={self.status}, time_to_change={self.time_to_change}."

class c_TrafficLight (Structure):
    _fields_ = [
            ("latitude", c_float),
            ("longitude", c_float),
            ("orientation", c_uint8),
            ("status", c_uint8),
            ("time_to_change", c_uint8)]

class RoadUser:

    def __init__ (self, latitude, longitude, speed, orientation, category):
        self.category=Categories(category)
        self.latitude=c_float(latitude).value
        self.longitude=c_float(longitude).value
        self.speed=c_uint8(speed).value
        self.orientation=c_uint16(orientation).value
        return

    def getAttributes (self):
        attrList = [self.latitude, self.longitude, self.speed, self.orientation, self.category.convert()]
        return attrList

    def __str__(self):
        return f"RoadUser with: latitude={self.latitude}, longitude={self.longitude}, speed={self.speed}, orientation={self.orientation}, category={self.category}."


class c_RoadUser (Structure):
    _fields_ = [
            ("latitude", c_float),
            ("longitude", c_float),
            ("speed", c_uint8),
            ("orientation", c_uint16),
            ("category", c_uint8)]