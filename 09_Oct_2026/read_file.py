'''file = open("employees.txt","r")

data = file.read()

print(data)

file.close()'''

###################################

'''file = open("employees.txt","r")

for line in file:
    print(line.strip())

file.close()'''

###################################

file = open("employees.txt","a")

file.write("104, Sara, Sales, 68000\n")

file.close()

# Unstructured Data -- Text, Audio, Video, PDF, Doc -- Azure Cloud

# Semi Structured Data -- JSON -- MongoDB

# Structured Data -- Tables -- My SQL