#With keyword

file = open("erin.txt","r")
data=file.read()
file.close()

with open("erin.txt","r") as f:
    data = f.read()
    print(data)

with open("erin.txt","r") as f:
    line1= f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    line5 = f.readline()
    line6 = f.readline()
    data=f.read()

    print("line1:",line1)
    print("line2:",line2)
    print("line3:",line3)
    print("line4:",line4)
    print("line5:",line5)
    print("line6:",line6)
    print("File Data",data)

with open("erin.txt","r") as f:
  readLines=f.readlines()
  print(readLines)