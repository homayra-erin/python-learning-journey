#List in python
Seafood=["Prawns","Shrimp","Squid","Octopus","Lobster"]
print(len(Seafood))
print(Seafood)

print("First value of the list:",Seafood[0])
print("First value of the list:",Seafood[3])

#List are mutable

Seafood[1]="Fish"
print(Seafood)

#Slicing
print(Seafood[1:])
Seafood.append("Starfish")
print(Seafood)
Seafood.sort()
print(Seafood)
Seafood.remove("Squid")
print(Seafood)
Seafood.pop(3)
print(Seafood)
Seafood.reverse()
print(Seafood)
Seafood.insert(1,"Prawn")
print(Seafood)
print(Seafood.index("Fish"))
print(Seafood[3])