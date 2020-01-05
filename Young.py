from User import CareallUser

class Young(CareallUser):

	def __init__(self,name,age,gender):
		CareallUser.__init__(self,name,age,gender)
		self.n_aged = 0
		self.agedlist = []
		self.choosen = []
	def add_aged(self,name):
		if len(self.agedlist)<4:
			self.agedlist.append(name)
			return True
		else:
			print("{} has reached the limit".format(self.name))
			self.status(False)
	def set_earning(self,earnings):
		self.earnings = earnings

	def get_earnings(self):
		return self.earnings
	#list of aged people the young is taking care of
	def show_aged(self):
		for name in agedlist:
			print name		
	def choose(self,t_agedlist):
		for aged in t_agedlist:
			if (aged.get_status):
				print ("Name = {}, Age = {}, Gender = {}".format(aged.name,aged.age,aged.gender))
				print(" ")
				print("{} Would you like to take care of {}. Type Yes or No".format(self.name,aged.name))
				d = raw_input()
				if d == 'Yes':
					self.choosen.append(aged)
			
			
			

