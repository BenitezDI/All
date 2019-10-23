import time
import os 

framelist = [
'''
    +---+
    o   |
   /|\\  |
   / \\  |
       ===''', '''
    +---+
   \\o/  |
    |   |
    \\\\  |
       ===''', '''
    +---+
         |     I'm FREEE!!
    o    |
   /|\\   |
   / \\  === ''' 


]
while True: 
	for frame in framelist:
		os.system("cls")
		print(frame)
		time.sleep(.2)