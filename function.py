from Young import Young
from Aged import Aged


A1 = Aged('Krishna',75,'Male')
A2 = Aged('Swati',60,'Female')
A3 = Aged('Arjun',70,'Male')
A4 = Aged('Arun',70,'Male')
A5 = Aged('Ajay',70,'Male')
Alist = [A1,A2,A3,A4,A5]

Y1 = Young("Ram",25,'Male')
Y2 = Young("Sita",23,'Female')
Ylist = [Y1,Y2]
d = {}

# the following code first askes young ones to choose amoung the old ones. Next it will ask the aged ones to choose from the young who choosed them. 

for young in Ylist:
	if (young.status):
		young.choose(Alist)
		for aged in young.choosen:
			if (aged.approve(young)):
				de = young.add_aged(aged)
				if(de):
					print("{} is taking care of {}".format(young.name,aged.name))
					aged.alot_young(young)
					print(" ")
					d.__setitem__(aged.name,young.name)
				else:
					print("{} has reached his limit. choose another one".format(young.name))
					young.set_status(False)
					aged.set_status(True)

#print(" ")
#for A in Alist:
#	print A.young.name,A.name
#print(" ")
#for Y in Ylist:
#	for A in Y.agedlist:
#		print A.name,Y.name

