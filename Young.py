from User import CareallUser

class Young(CareallUser):

	def __init__(self,name,age,gender):
		CareallUser.__init__(self,name,age,gender)
		self.n_aged = 0
		self.agedlist = []
		self.choosen = []
		self.status = True
	def add_aged(self,name):
		if len(self.agedlist)<4:
			self.agedlist.append(name)
			return True
		else:
			return False
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
				print("{} Would you like to take care of {}.".format(self.name,aged.name))
				d = self.decide(aged)
				
	def decide(self,aged):
		print("Type Yes or No")
		d = raw_input()
		if d == 'Yes' or d == 'yes':
			self.choosen.append(aged)
		elif d == 'No' or d == 'no':
			pass
		else: 
			return self.decide(aged)















