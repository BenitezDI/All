myWord = "Peach"

choice = input("Take a guess of what the word might be: ")

if choice == myWord:
	print("Good job, you got it! ")

else: 
	print("Sorry, that's not right")

# How to check if a letter is in a word 
letter = input("Type a letter")
if letter is myWord:
	print("That letter is definetly in the word!")
else: 
	print("I'm sorry but that letter is not in the word")

count = 0 
for s in myWord:
	if s == letter:
		print(count)
	count += 1