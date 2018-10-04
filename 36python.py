p=input("enter r or p or s:")
d=['r','p','s']
import random
c=random.choice(d)
if(p=='c'):
	print("tie play again")
elif(c=='r'):
	if(p=='p'):
		print("p wins")
	else:
		print("c wins")
elif(c=='p'):
	if(p=='s'):
		print("p wins")
	else:
		print("c wins")
	elif(c=='s'):
		if(p=='r'):
			print("p wins")
	else:
		print("c wins")




