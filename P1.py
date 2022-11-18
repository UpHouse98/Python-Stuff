from random import randint, random, randrange
import math

def randNum():    
    return math.floor(random()*10+1)

while True:
    print("Hello! Welcome to the quessing game \n In this game you will try to guess the missing number between 0 and 10!")
    x = str(randNum())
    #print(x)
    guess = input("Take a guess: ")
    print(guess)

    while guess != x:
        guess = input("Another one:")
    else:
        print("Good guess!")
    





    


