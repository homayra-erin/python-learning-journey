#1.Create a class Car with attribute brand="Scorpio".

class car:

   brand="Scorpio"

obj1=car()
print("Brand name is - ", obj1.brand)

#2.Create a class Laptop w attribiutes: brand,RAM,price.Create 2 objects with diff. values.

class Laptop:
   brand="HP"
   Ram="8 GB"
   price="80k"

obj1=Laptop()
obj1.brand="Asus"
obj1.Ram="16GB"
print(f"The laptop brand is {obj1.brand} with {obj1.Ram} Ram, price is {obj1.price}.")

obj2=Laptop()
obj2.price="70k"
print(f"The laptop brand is {obj2.brand} with {obj2.Ram} Ram, price is {obj2.price}.")

#3.Create class Student that takes 3 marks & has a method average().

class Student:

    def __init__(self,name,listOfMarks):
       self.name = name
       self.listOfMarks=listOfMarks

    def average(self):
        sum =0
        for i in self.listOfMarks:
             sum = sum + i
             average=sum/3
        print("Here is the average mark",average)
   

S1=Student("Erin",[90,98,99])
S1.average()

      
   