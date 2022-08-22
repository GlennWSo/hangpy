from hang_lib import HANGMANPICS as PICS
from clear import clear
from stringhelp import replacer
    
class Game():
    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.word = "".join("_" for _ in secret)
        self.used = ""
        self.mistakes = 0
    
    def greet(self):
        print("Welcome to Hang")
        print("Guess the word or be hung!")

    def draw(self):
        clear()
        self.greet()
        
        if self.mistakes > 0:
            print(PICS[self.mistakes])   
            print("Mistakes: ", ", ".join(c for c in self.used))
        print("Enter a missing char!")
        print("The word: ", self.word)
    
    def ask(self) -> str:
        guess = input().upper()
        if len(guess)<1:
            print("Try again")
            guess = self.ask()
        return guess
    

    def check(self, guess: str):    
        for char in guess:
            if char in self.secret:
                for i, c in enumerate(self.secret):
                    if c == char:
                        self.word = replacer(self.word, c, i)
            else:
                self.mistakes += 1
                self.used += char
            
    def play(self):
        while self.mistakes < 7:
            self.draw()
            guess = self.ask()
            self.check(guess)
            if self.word==self.secret:
                self.draw()
                print(self.secret)
                print("You won!")
                return
        
        print("Game over!")
        exit(1)
        
if __name__ == "__main__":
    import sys
    
    match sys.argv:
        case [*_, "-s", secret]:
            game = Game(secret)
        
        case [_, secret]:
            game = Game(secret)
        
        case _:
            game = Game("byxor")

    game.play()