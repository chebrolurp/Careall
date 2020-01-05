from Young import Young
from Aged import Aged


A1 = Aged('Krishna',75,'Male')
A2 = Aged('Swati',60,'Female')
A3 = Aged('Arjun',70,'Male')
Alist = [A1,A2,A3]

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
				if(young.add_aged(aged)):
					print("{} is taking care of {}".format(young.name,aged.name))
					aged.alot_young(young)
					print(" ")
					d.__setitem__(aged.name,young.name)
				else:
					print("choose another one")

#print(" ")
#for A in Alist:
#	print A.young.name,A.name
#print(" ")
#for Y in Ylist:
#	for A in Y.agedlist:
#		print A.name,Y.name

