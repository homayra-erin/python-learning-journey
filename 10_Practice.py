#Question:1.Ask the user for their 3 favourite movies & store them in a list.
movie1=input("Enter your first choice: ")
movie2=input("Enter your 2nd choice: ")
movie3=input("Enter your 3rd choice: ")

movieList=[movie1,movie2,movie3]
print(movieList)

#2.Create tuple of marks (87,64,33,95,76) & print the highest & lowerst marks using max() & min()
marks=(87,64,33,95,76)
print(max(marks))
print(min(marks))

#3.Write a program to check grade based on marks (A/B/C/D) using if-elif-else.
marks=64

if(90<marks):
    print("A")


elif(80<marks):
    print("B")


elif(70<marks):
    print("C")


elif(60<marks):
    print("D")

else:
    print("F")
