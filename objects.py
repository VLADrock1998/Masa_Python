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
		self.category=c_uint8(category)

	def getCategory(self):
		return self.category

	def convert(self):
		return Categories.categories_list.get(self.category)
		
		
	def printCategories ():
		for c in Categories.categories_list: 
			print(c," ",Categories.categories_list.get(c))
	
	def __str__(self):
		return self.category
    
class LightStatus:
    
    statuses_list={
            "L_green":c_uint8(1).value,
            "L_yellow":c_uint8(2).value,
            "L_red":c_uint8(3).value}
		
    def __init__(self, status):
        if status not in LightStatus.statuses_list:
            print("ERRORE!!!!")
            return
        self.status=c_uint8(status)
        
    def getStatus(self):
        return self.status
    
    def convert(self):
        return LightStatus.statuses_list.get(self.status)
    
    def printStatuses():
        for s in LightStatus.statuses_list:
            print(s," ",LightStatus.statuses_list.get(s))
            
    def __str__(self):
        return self.status
		
class TrafficLight:
    
    def __init__(self, latitude, longitude, orientation, status, time_to_change):
        self.status=LightStatus(status)
        self.latitude=c_float(latitude).value
        self.longitude=c_float(longitude).value 
        self.orientation=c_uint8(orientation).value
        self.time_to_change=c_uint8(time_to_change).value
        
    def serializeObject (self):
        all_param = []
        all_param.append(self.latitude)
        all_param.append(self.longitude)
        all_param.append(self.orientation)
        all_param.append(self.status.convert())
        all_param.append(self.time_to_change)
        return all_param
    
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
    
    def serializeObject (self):
        all_param = []
        all_param.append(self.latitude)
        all_param.append(self.longitude)
        all_param.append(self.speed)
        all_param.append(self.orientation)
        all_param.append(self.category.convert())
        return all_param

    def __str__ (self):
        R="latitude: "+str(self.latitude)+"\nlongitude: "+str(self.longitude)+"\nspeed: "+str(self.speed)+"\norientation: "+str(self.orientation)+"\ncategory: "+str(self.category)
        return R
    
class c_RoadUser (Structure):
    _fields_ = [
            ("latitude", c_float),
            ("longitude", c_float),
            ("speed", c_uint8),
            ("orientation", c_uint16),
            ("category", c_uint8)]