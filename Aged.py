from User import CareallUser

class Aged(CareallUser):
	def __init__(self,name,age,gender):
		CareallUser.__init__(self,name,age,gender)
	
	# young who is taking care of aged
	def alot_young(self,young):
		self.young = young

	def get_young(self):
		print self.young

	def set_funds(self,funds):
		self.funds = funds

	def get_funds(self):
		return self.funds

	def approve(self,young):
		
		if self.status == True:
			print ("Name = {}, Age = {}, Gender = {}".format(young.name,young.age,young.gender))
			print(" ")
			print("{} Would you like to be taken care by {}. Say Yes or No".format(self.name,young.name))
			d = raw_input()
			if d =='Yes':
				self.set_status(False)
				return True
			else:
				return False

