from hang_lib import HANGMANPICS as PICS
from clear import clear
from time import sleep


def replacer(s, newstring, index):
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

    
class Game():

    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.word = "".join("_" for _ in secret)
        self.used = ""
        self.mistakes = 0
    
    def greet(self):
        clear()
        print("Hello Ladies!")
        print("Welcome to hang!")
        print("Guess the word or be hung!")

    def _ask(self) -> str:
        if len(self.used) > 0:
            print(PICS[self.mistakes])   
            print("Mistakes: ", [c for c in self.used])

        print("Enter a missing char!")
        print("The word: ", self.word)

        char = input().upper()

        if len(char)<1:
            print("Try again")
            char = self._ask()
        return char
    

    def _check(self, char: str):    
        if char not in self.secret:
            self.mistakes +=1
            self.used += char
            return False
        return True
            
    def play(self):
        while self.mistakes < 7:
            clear()
            self.greet()
            char = self._ask()
            if self._check(char):
                for i, c in enumerate(self.secret):
                    if c == char:
                        self.word =  replacer(self.word, c, i)
                
                if self.word==self.secret:
                    clear()
                    print(self.secret)
                    print("You won!")
                    sleep(5)
                    break
        
        print("Game over!")
        
if __name__ == "__main__":
    import sys
    
    match sys.argv:
        case [*_, "-s", secret]:
            game = Game(secret)
        
        case _:
            game = Game("byxor")
    game.play()