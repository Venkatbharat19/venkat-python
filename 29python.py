while True:
	a=(input("click r to roll dies:"))
	if(a=="r"):
		import random
		r=random.randint(1,6)
		print(r)
	else:
		print("bye")
		break

