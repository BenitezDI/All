#Hint 1
myString = "arizona"
mylist = list(myString)
print(mylist)
secret = []

#Hints 2
for a in mylist:
	secret.append("_")

print(secret)

#Hint 3 

secret[2] = "i"
print(secret)