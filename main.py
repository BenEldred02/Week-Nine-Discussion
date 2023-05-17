# This is a header for the application.
# You should read this header and insert your name and your date below as part of the peer review.
# This is a typical part of any program
# Reviewed By: Benjamin Eldred
# Review Date: 05/09/2023
# Below is a simple program with several issues.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
  #This section has invalid indentation. The appropriate indentation should be done in this manner:
    while cave != '1' and cave != '2':  
        #while cave != '1' and cave != '2':
            #This formatting is odd and confusing to the user in the output stage. This would be my recommendation:
            cave = input("Which cave will you go into? ('1' or '2'): ")
            print()
            #print('Which cave will you go into? (1 or 2)')
            #cave = input()
            
    #This 'caves' variable has not been assigned to anything. On Line 19, 'cave' was used and needs to be used again here. This should be coded as:
    return cave
    #return caves

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
      #This 'print' function is missing the parentheses. The correction should look like this: 
        print('Gobbles you down in one bite!')
        #print 'Gobbles you down in one bite!'


displayIntro()
#The capitalization is important when referencing variables and their values. This should be written as:
caveNumber = chooseCave()
#caveNumber = choosecave()
checkCave(caveNumber)
#Mispelling here in the end message. Try this:
print()
print("Thank you for playing!")
#print("Thanks for planing")