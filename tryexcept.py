import os

try:
    with open("homayra.txt","r") as f:
        listOfLines=f.readlines()
        print("Output of readLines Function",listOfLines)
        print("Number of Lines in Function",len(listOfLines))

except:
    print("That files does not exist")