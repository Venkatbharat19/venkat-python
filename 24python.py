#take input from the user and print the tables upto 10
n=int(input("Enter value for a"))
for n in range (1,n+1):
	for a in range (1,11):
		print(n,"*",a,"=" ,n*a)
	print("\n")
