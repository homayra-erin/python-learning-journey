#1.Write code to open a file named mydata.txt in text mode.

file=open("MyData.txt","rt")
data=file.read()

print("Here is the brief:\n",data,sep="")

#2.Write a program to read a text from a give file certificate.txt & find whether it contains the word live.
file=open("Certificate.txt","r")
dataCertificate=file.read()

dataCertificate=dataCertificate.lower()

if "live"in dataCertificate:
    print("Yes the live word is present in this file")
else:
    print("No")

#3.What happens if you open a non-existing file in "r" mode?

# file=open("myfile.txt","r")
# data=file.read()

# print("Here is the brief of the file:\n",data,sep="")

#If a non-existing file is opened in "r" mode, Python raises a FileNotFoundError because the file does not exist and read mode cannot create a new file.

#4.Open a file in write mode.
reportfile=open("report.txt","a")
reportfile.write("I want to change my life.")

reportfile=open("erin.txt","x")

