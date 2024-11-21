myfile=open("devices.txt","r")
for item in myfile:
    print(item.strip())
myfile.close()
