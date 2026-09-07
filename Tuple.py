#Tuple basics

myTuple=(78,90,75)
studentTuple=("Khushi","Dipi","Bonni","Erin")
print(len(studentTuple))

#Tuples are immutable
#studentTuple[1]="Chaity"

print(studentTuple[2])

#Empty Tuple
emptyTuple=()

#Single Tuple
singleTuple=(1,)

print(type(emptyTuple))
print(type(singleTuple))
print(studentTuple.index("Bonni"))
print(studentTuple.count("Erin"))
print(studentTuple[2])