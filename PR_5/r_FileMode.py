# file = open("demo.txt",'r')
# print("Reading entire file")
# print(file.read()) #reading entire file

# print("Reading only particular lines of file")
# print(file.read(2))

# print("Reading one line of file")
# print(file.readline())

# print("Reading entire file")
# print(file.readlines())

# with open("demo.txt",'w') as file1:
#     file1.write("Namrata Daphale\n")
#     file1.write("Python programming\n")
#     print("Data written!")

# with open("demo.txt",'r') as file1:
#     print(file1.read())

# with open("demo.txt",'a') as file1:
#     file1.write("Appending data\n")
#     print("Data appended!")

# with open("demo.txt",'r') as file1:
#     print(file1.read())

# with open("demo.txt",'r') as file1:
#     file1.seek(5)
#     print(file1.read())

# with open("demo.txt",'r+') as file1:
#     file1.write("I'm Namrata ")
#     file1.seek(0)
#     print(file1.read())#overwrites the data 

# with open("demo.txt",'w+') as file1:
#     file1.write("demo77")
#     file1.seek(0)
#     print(file1.read()) 

# with open("demo.txt",'a+') as file1:
#     file1.write("Data Appended")
#     file1.seek(0)
#     print(file1.read())

# with open("demo1.txt",'w+') as file1:
#     file1.write("New File")
#     file1.seek(0)
#     print(file1.read())

with open("demo.txt",'r') as file1:
    print(file1.tell())
    file1.read()
    print(file1.tell())