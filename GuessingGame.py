secretWord="python"
guess=""
guessesNumber=3
hasAnswered=False

while guess!=secretWord and guessesNumber>0:
    guess = input("Guess word: ")
    guessesNumber-=1
    if(guess==secretWord):
        hasAnswered=True

if hasAnswered==True and guessesNumber>0:
    print("You win!")
else:
    print("You lose!")