#Function practice.
# #1.Write a function named welcome-message() that prints "Welcome to Python Programming!" three times.
#Function Definition
def welcome_message():
    print("Welcome to Python Programming!")

#Calling the function
welcome_message()#Function is being called.
welcome_message()#Function is being called.
welcome_message()#Function is being called.
welcome_message()#Function is being called.

#2.Define a function inspire() that prints a motivational quote with your name.
#Function Definition
def inspire():
    Quote="I did not learn to give up."
    author="Erin"
    print(f'"{Quote}"\n~{author}')

#Calling the function
inspire()

#Importance:1.Make code more redable.2.Avoid redundancy.
 
#3.Explain what happens if you call a function before defining it
OSError() #Not defined
# Function Calling with no Arguments
#Solution:
def solution():
    print("It is Defined")

solution()

#4.Write a function show_age(name,age) that prints "Homayra Erin is 21 years old."
def show_age(name="Happy",age=42):

    print(f"{name} is {age} years old.")

show_age("Homayra Erin",21)
show_age()
show_age("Diya",23)

#5.Create a function add numbers(a,b) that prints both the Sum & Difference.
def numbers(a=5,b=2):
    print("Sum=",a+b,"Difference=",a-b)

numbers()

#6.Write a function fav_food(food) that prints "Saumya loves <food>".
def fav_food(food="Salad"):
    print(f'"Saumya loves {food}".')
fav_food()

#7.Write a program with a local variable score inside a function & a global one outside.
score = 50   # Global variable

def show_score():
    score = 90   # Local variable
    print("Inside function:", score)

show_score()

print("Outside function:", score)

#8.Create a program using global keyword to modify a variable from inside a function.
score = 50   # Global variable

def update_score():
    global score
    score = 90

print("Before:", score)

update_score()

print("After:", score)

#9.Explain the difference b/w local & global scope in your own words.
# Local scope means a variable can be used only inside the function where it is created. We cannot access it from outside the function.

# Global scope means a variable is created outside a function and can be accessed from different parts of the program, including inside functions.



