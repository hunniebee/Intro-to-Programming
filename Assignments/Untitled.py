file_object = open("datafile.txt", "r")
data = file_object.read()
file_object.close()
x = data.split("\n")
file_object_2 = open("datafile.txt", "w")
for i in x:
    if len(i) % 2 == 0:
        file_object_2.write(i + "!\n")
    else:
        file_object_2.write(i + "?\n")
         
file_object_2.close()
