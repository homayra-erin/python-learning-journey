#Loops Basics Practice Questions
#1.Write a Python program to print numbers from 1 to 10 using a while loop.

i=1

while(i<=10):
    print(i)
    i+=1
print("First Question completed")

#2.Write a Python program to print numbers from 10 to 101 using a while loop.

i=10

while(i>=1):
    print(i)
    i-=1
print("Second Question completed")

#3.Write a program to print all even numbers b/w 1 & 50 using a while loop.
#Hints:Use the modulus operator % to check for even numbers.
i=1
while(i<=10):
    if(i%2==0):
      print(i)
    i=i+1
print("Third Question completed")

#4.Write a program that prints the sum of first n natural numbers.
#For examples,if n=5, the output should be 1+2+3+4+5=15.
#(Hint:Keep a running total inside the loop)
n=int(input("Enter a number: "))
sum=0
while n>=1:
    sum=sum+n
    n=n-1

print("Sum= ",sum)
print("n= ",n)
print("End!")

#5.Write a program to print this patterns using a while loop:
#*
#**
#***
#****
n=1
while n<=4:
    print("*"*n)
    n=n+1

print("End!")
    
#6.Saumya wants to print her name 5 times, but each time w a number in front of it.Write a program using a while loop that prints:
i=1
while i<=5:
    print(f"{i}.Saumya Singh")
    i=i+1

#7.Write a program to print the multiplication table any number using a while loop.
#Hint:start i=1 & run the loop until i<=10.
n=int(input("Enter the number: "))
i=1
while i<=10:
    print(f"{n}*{i}={n*i}")
    i=i+1

