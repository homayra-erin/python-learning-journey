#Question on slicing
#Write a program that takes your favorite food name as input & prints:
food="Seafood"
print("My favourite food is: ",food)
#1.The middle 3 characters
print("The middle 3 characters: ", food[1:4])
#2.The last 2 characters
print("The middle 2 characters: ", food[5:])

#Taking input
color=input("Enter my fav color: ")
mid=len(color)//2
#1.The middle 3 characters
print("The middle 3 characters: ", color[mid-1:mid+2])
#2.The last 2 characters
print("The middle 2 characters: ", color[mid+1:])

