print("Welcome to the To Do List! ")
Todolist = []

while True: 
	print(" Enter a to add an item ")
	print(" Enter r to remove and item ")
	print(" Enter p to print the list ")
	print(" Enter q to quit ")
	choice = input(" Make your choice: ")

	if choice == "q":
		break
	elif choice == "a":
		#Add and item to the list
		need = input("What do you need added on the list?")
		Todolist.append(need)

	elif choice == "r":
		#Remove an item from the list
		Remove = input("What do you want off the list? ")
		Todolist.remove(Remove)
		
	elif choice == "p":
		#Print the list 
		Item = 1 
		for anItem in Todolist:
			print(" Item "  + str(Item) + " is " + anItem) 
			Item += 1
	
	else:
		print("Sorry that wasnt a choice, try again")