#1.Read only gthe first line of erin.txt.

with open ("erin.txt","r") as f:
    firstLine=f.readline()
    print( firstLine)

#2.Print how many lines are present in erin.txt

with open ("erin.txt","r") as f:
    totalLines=f.readlines()
    print("Total Lines",len(totalLines))

#3.Write your name & class into a file named intro.txt
file=open("intro.txt","x")
data=file.write("I'm Erin.I,m pursuing bsc in cse")

#4.Create a file goal.txt and write 3 goals for this month.
file=open("goal.txt","x")
goal = file.write("(1)Master in Python.(2)Academic Focus.(3)No fastfood.")

#5.Append "Complete" to an existing file goal.txt.

file=open("goal.txt","a")
data=file.write("Complete")

###copy file

import shutil
shutil.copy("goal.txt","schedule.txt")

###rename file

import os
os.rename("erin.txt","Homayra.txt")
import os
os.rename("Homayra.txt","erin.txt")

###Delete file
with open("delete.txt","x") as f:
    data=f.write("I won't exist")

import os
os.remove("delete.txt")

