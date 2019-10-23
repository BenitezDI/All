#Make a list 
myClasses = ["Algebra", "English","World History"]
print(myClasses)

#Add an item to the list 
#Append or insert 
#Append will know to back of the lists

myClasses.append("Coding")
print(myClasses)
favClass = input("What is your favorite class? ")
myClasses.append(favClass)
print(myClasses)

#Insert
myClasses.insert(3, "Art")
print(myClasses)
#Overwrite/replace
myClasses[4] = "Science"
print(myClasses)

#Remove list items 
#Remove,pop
#Remove will remove a specific items 
myClasses.remove("Science")
#myClasses.remove("Lunch")
#Pop will remove the item at a specific index
myClasses.pop() #Erases the last item
print(myClasses)
myClasses.pop(1)
print(myClasses)
#Len - it returns the length of a list
print("myClasses is " + str(len(myClasses)) + " items long ")

print(myClasses[len(myClasses) - 1])

# Loop through a list
count = 1
for aClass in myClasses:
	print("Item " + str(count) + " is " + aClass)
	count = count + 1 

numbers = [ 1, 3, 5, 7, 9, 11, 13, 15 ]

#Challenge: Loop through the lists add the numbers and print the sum


total = 0
for number in numbers:
	total += number

print(total)
#.append("cooking")

if "cooking" in myClasses:
	print("Have fun")
else: 
	print("Okay then,byeee")

