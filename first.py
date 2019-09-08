import random


number = random.randint(1,10)
tries=1
uname=input("Hello, What is ur user name?")



print("Hello",uname+".",)



question=input("Would you like to play a game(Y/N)?")

if question == 'N' or question == 'n':
    print("Ok.. Bye")

if question == 'Y' or question == 'y':
    guess=int(input("Can You guess the number I am thinking?"))
   
    while guess!=number:
        tries+=1
        if guess>number:
             print("Guess Lower...")
        if guess<number:
             print("Guess Higher")      
        guess=int(input("Thats wrong! Try Again?"))
       
    print("well done you guessed it right in",tries,"tries")
