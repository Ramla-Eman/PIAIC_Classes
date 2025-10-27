# complex way
# file =open("example.txt", 'w')
# file.write("hi i am rizwan ahmed")
# file.close()

# file2 =open("example.txt", 'a')
# file2.write("hi i am ramla Eman")
# file2.close()

# file3 = open("example.txt", "r")

# res = file3.read()
# print("response", res)
# file3.close()

# easy way

with open("example.txt", "r") as file:
    result = file.read()
    print("result", result)