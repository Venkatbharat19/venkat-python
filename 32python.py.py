def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mult(a,b):
	return(a*b)

def divide(a,b):
	return(a/b)

i=int(input("Enter value of a:"))
j=int(input("Enter value of b:"))
o=(input("what do you want to do? +,-,x,/")

if(o=='+'):
	res=add(i,j)
elif(o=='-'):
	res=sub(i,j)
elif(o=='x'):
	res=mult(i,j)
elif(o=='/'):
	res=divide(i,j)
print(res)