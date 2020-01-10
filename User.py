class CareallUser:

	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender
		self.status = True
	def set_id(self,ID):
		self.id = ID
	
	def get_id(self):
		return self.id

	# Status tells about their availability to take care or to be taken care of.
	def get_status(self):
		return self.status
	
	def set_status(self,status):			
		self.status = status

	def get_rating(self):
		return self.rating
	
	def set_rating(self,rating):
		self.rating = rating

