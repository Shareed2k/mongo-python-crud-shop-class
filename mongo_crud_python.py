from pymongo import MongoClient
import math 

#ob = list(col.find())

#print ob[0]['name']
#for i in col.find():
 #   print i

class CRUD:
	
	def __init__(self):
		self.client = MongoClient()
		self.db = self.client.test
		self.col = self.db.testdata
		
	def insert(self, elems=()):
		self.col.save(elems)
		
	def read(self, elems=()):
		return self.col.find(elems)
		
	def update(self, elemsA=(), elemsB=()):
		self.col.update(elemsA, elemsB)
		
	def delete(self, elems=()):
		self.col.remove(elems)
		
	# lats use the haversine formula to calculate the great-circle distance between two points 
	def distance(self, p1lat, p1lon, p2lat, p2lon):
		# a = sin(F/2) + cos(F1).cos(F2).sin(G/2)
		# c = 2 * atan2(sqrt(a), sqrt(1-a))
		# d = R * c
		
		# where	F is latitude, G is longitude
		# R is earth's radius (mean radius = 6,371km)
		# note that angles need to be in radians to pass to trig functions!
		try:
			r = 6371
			dlat = math.radians((p2lat - p1lat))
			dlon = math.radians((p2lon - p1lon))
			p1lat = math.radians(p1lat)
			p2lat = math.radians(p2lat)
		
			a = (math.sin(dlat / 2) * math.sin(dlat/2) + math.sin(dlon / 2) * math.sin(dlon / 2)	\
			* math.cos(p1lat) * math.cos(p2lat))
		
			c = (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))	
			d = r * c
			return d
		except:
			return 0
			
	def readShops(self, elems=()):
		return self.db.shop.find(elems)	
			
	def proximityShops(self, p1lat, p1lon):
		try:
			b = self.readShops({})
			minlat = b[0]['location']['lat']
			minlon = b[0]['location']['lon']
			minD = self.distance(p1lat, p1lon, minlat, minlon)
			cur = None
			for i in b:
				if(min(minD, self.distance(p1lat, p1lon, i['location']['lon'], i['location']['lat'])) < minD):
					minD = self.distance(p1lat, p1lon, i['location']['lon'], i['location']['lat'])
					print minD
					cur = i
			items = self.read({'external_id': cur['item_external_id']})
			for i in items:
				print i
		except:
			return 0
		
obj = CRUD()
#obj.insert({'id':2,'name':'Bob','grade':'B'})
#obj.update({'id': 2}, {"$set": {'id': 1}})
#obj.delete({'id': 2})
#b = obj.read({'name': 'Bob'})
#for i in b:
#	print i
	
#print obj.distance(32.007907, 34.77079, 31.8952746, 34.98807)
obj.proximityShops(32.007190, 34.768505)
