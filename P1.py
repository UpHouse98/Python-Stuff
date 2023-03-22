from random import random
import math

print("Hello! Welcome to the guessing game!\nTry to guess the missing number between 0 and 10!")
x = lambda num : str(math.floor(random()*10+num))
guess = input("Take a guess: ")
while guess != x(1):
    guess = input("Another one:")
else:
    print("Good guess!")
