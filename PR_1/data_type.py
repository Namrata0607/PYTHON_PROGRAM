print("text data type : ")
str1 = "Namrata"
print("name : ",str1)

print("\nnumeric data type : ")
num1 = 10
print("type of num1 : ",type(num1))
num2 = 10.10
print("type of num2",type(num2))
num3 = 1j
print("type of num3",type(num3))

print("\nsequence data type : ")

lst = [1,2,3,4,5]
print("elements in list",lst)
tpl = (1,2,3,4,5)
print("elements in tpl",tpl)
rng = range(5)
print("range : ",rng)

print("\nmapping data type")
dit = {1:"shamal",2:"jyoti",3:"vishval"}
print("elements in dict : ",dit)

print("\nset data type")
st1 = {1,2,3,4,5}
print("elements in set : ",st1)
st2 = frozenset({1,2,3,4,5})
print("elements in set : ",st2)

x = bytearray(1)
print("byte array: ",x)

x,y,z = input().split()
print(z)	
