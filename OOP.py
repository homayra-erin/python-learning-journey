#class creation
class Vehicle:
    color="Black"#attributes
    petrolOrDiesel="petrol"#attributes
    mileage="10"#attributes

    def start(self):  #methods
        print("When you press clutch & accelerator then vehicle then vehicle is started.")


#Object Creation
car=Vehicle()
print(car.color)
bike=Vehicle()
print(bike.color)
aeroplane=Vehicle()
print(aeroplane.mileage)
print(aeroplane.color)
car.start()

#we created one class & 3 objects of that class

#The __init__() Constructor
class Student:
    schoolName="EWU"

    def __init__(self,name,course):
    #    print("Whenever a new object is created I'm called automatically")
       self.name=name
       self.course=course 
     
student1 = Student("Erin","Btech") #init method called
print("Student 1 Name", student1.name)
print("Student 1 course", student1.course)
student2 = Student("Hasin","BSc")
print("Student 2 Name", student2.name)
print("Student 2 course", student2.course)

