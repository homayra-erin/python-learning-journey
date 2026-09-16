#OOP Practice

#Student Class
#1.Create class Student with name,class,marks.Add method get_percentage().

class Student:
    # 1. The constructor method 


    def __init__(self, name, cls, marks):
        self.name = name
        self.cls = cls        # 'class' is a reserved keyword in Python, so we use 'cls'
        self.marks = marks    # Assumes 'marks' is a list of numbers

    # 2. Method to calculate and return the percentage
    def get_percentage(self):
        if not self.marks:    # Check if the list is empty to avoid division by zero
            return 0
        total_marks = sum(self.marks)
        max_marks = len(self.marks) * 100  # Assumes each subject is out of 100
        percentage = (total_marks / max_marks) * 100
        return percentage

# --- Testing the Class ---

# Creating an instance of Student (passing name, class, and a list of marks)
s1 = Student("Rahim", "Class 10", [85, 90, 78, 92])

# Printing details
print(f"1. Name: {s1.name}")
print(f"2. Class: {s1.cls}")
print(f"3. Percentage: {s1.get_percentage():.2f}%")

#Creator Portfolio
#2.Create class Creator with attribute(name,username).Add method bio().

class Creator():

    def __init__(self,name,username):
        self.name=name
        self.username=username

    def bio(self):
        print("Here is my portfolio")

u1=Creator("Homayra Erin","erin.homayra")

u1.bio()
print(f"Name:{u1.name} & Username:{u1.username}")

#Food Order
#3.Create class FoodOrder with item name,quantity,price.Add method to calculate bill.

class FoodOrder:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

    def calculateBill(self):

        
        sum=self.quantity * self.price

        return sum
        


Obj1=FoodOrder("Rice",3,300)

print("Total bill:",Obj1.calculateBill())

#Employee Salary Manager
#4.Add method to increase salry by a percentage.

class Salary:
    def __init__(self,salary):
        self.salary = salary

    def get_percentage(self):
        