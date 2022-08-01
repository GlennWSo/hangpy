from hang_lib import HANGMANPICS as PICS
from clear import clear
from time import sleep


   

secret = "tulpan".upper()    

word = "".join("_" for _ in secret)

counter = 0


def ask():

    print("The word: ", word)
    print("Enter a missing char!")
    char = input().upper()

    if len(char)<1:
        print("Try again")
        char = ask()
    return char
    

def escalate(counter) -> int:    
    if char not in secret:
        clear()
        print(PICS[counter])   
        counter +=1
    return counter        
        
def replacer(s, newstring, index):
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


clear()
print("Welcome to hang!")
while counter < 7:
    char = ask()
    
    if char in secret:
        for i, c in enumerate(secret):
            if c == char:
                word =  replacer(word, c, i)
                
        if word==secret:
            print("win")
            sleep(5)
            break
    
    else:
       counter =  escalate(counter)
        
        
print("Game over!")