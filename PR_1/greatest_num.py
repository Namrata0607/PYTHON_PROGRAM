# program for greatest number among 3 num

print("enter three numbers : ")
x = int(input())
y = int(input())
z = int(input())

if(x>y and x>z):
	print("greatest number is : ",x)
elif(y>x and y>z):
	print("greatest number is : ",y)
else:
	print("greatest number is : ",z)

