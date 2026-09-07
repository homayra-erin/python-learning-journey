#Functions Basic.
# a = 3
# b= 8
# sum = a+b
# print(sum)

# #Some more lines of code

# avg=(a+b)/2
# print(avg)

# #.....100 line of code

def sumFunc():
    a=4
    b=8
    sum=a+b
    print("Sum:",sum)

# #.....100 line of code

sumFunc()

# #.....100 line of code

sumFunc()

#We can use the parameter name while passing values.
def student_info(name, age):
    print(name,"is",age,"years old.")
student_info(name="Erin",age=21)

#None in python
def greet():
    print("Hello Erin")

result = greet()
print(result)