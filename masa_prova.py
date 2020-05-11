from ctypes import c_uint8
from ctypes import c_uint16
from ctypes import c_uint32
from ctypes import c_uint64
from ctypes import c_float
from enum import Enum

class Categories:
	
	categories_list={
		"C_person":14, 
		"C_bycicle":1,
		"C_car":6,
		"C_motorbike":13,
    		"C_bus":5,
    		"C_marelli1":20,
    		"C_marelli2":21,
    		"C_quattroporte":30,
    		"C_levante":31,
    		"C_rover":40}

	def __init__ (self, category):
		if category not in Categories.categories_list:
			print("ERRORE!!!!")
			return
		self.category=category

	def getCategory(self):
		print(self.category)

	def convert(self):
		return Categories.categories_list.get(self.category)
		
		
	def printCategories ():
		for c in Categories.categories_list: 
			print(c," ",Categories.categories_list.get(c))

	#def printCategories (self):
	#	for c in Categories.categories_list: 
	#		print(c," ",Categories.categories_list.get(c))
	
	def __str__ (self):
		return self.category
		
		
				
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

	def __str__ (self):
		R="latitude: "+str(self.latitude)+"\nlongitude: "+str(self.longitude)+"\nspeed: "+str(self.speed)+"\norientation: "+str(self.orientation)+"\ncategory: "+str(self.category)
		return R

class masa_prova:

	def __init__(self,cam_idx, t_stamp_ms, num_objects):
		self.cam_idx = c_uint32(cam_idx).value
		self.t_stamp_ms = c_uint64(t_stamp_ms).value
		self.num_objects = c_uint16(num_objects).value

	def printMessage (self):
		print(self.cam_idx)
		print(self.t_stamp_ms)
		print(self.num_objects)
