#Name: Dayanara 
#Period 6
#review.py

#Variable declaration and assignment 
myVariable = " Dayanara" # string v
myNumber = 12 #int v 
MyDecimal = 12.6 #float variable 


#While Loop 
x = 1
while x <= 10:
	print(x)
	x += 1

#Challenge: Make a while loop to count down from 100 to 1 
x = 100 
while x >= 1:
	print(x)
	x -= 1


#String concatenation 

string1 = "Hello "
string2 = "World"
print(string1 + string2 + "!")

#Challange: Make a variable with your favorite movie 
#Print "My favorite movie is"

favMovie = "After"
print("My favorite movie is After")

#Input 

#Example
yourName = input("What is your name ")
print("Hello " + yourName)

#Challenge 
#Prompt for favorite song 
#Print your favorite song 

yourSong = input("What is your favorite song? ")
print("Your favorite song is " + yourSong)


#Casting 

myNum = input("Enter a number ") #myNum is a string type
myNum = int(myNum) + 10 #myNum is not an int S
print("The number is" + str(myNum))

ex1 = input("Enter a number") 
ex2 = input("Now another")
ex3 = int(ex1) + int(ex2)
print("The answer is" + str(ex3))


#if and if/else 
num = int(input("What is your number: "))

if num > 100:
	print("Your number is more than 100")

elif num == 100:
	print("Your number is equal to 100")
else: 
	print("Your number is less than  to 100")



bday = input(" Is it your birthday? ")

if bday == "yes":
	print("Happy birthday")
elif bday == "no":
	print("Welp hope you have a good day")
else: 
	print("You didnt put yes or no") 