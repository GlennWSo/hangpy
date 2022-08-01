from hang_lib import HANGMANPICS as PICS
from clear import clear
from time import sleep


   

secret = "tulpan".upper()    

word = "".join("_" for _ in secret)


print("The sercret:", secret)

print("The word: ", word)
print("Guess a char!")


