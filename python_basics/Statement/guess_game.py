#This is for Infinte Time Chances
import random
"""n = random.randint(1, 9)
guess = int(input("Enter an integer from 1 to 9: "))
while n != "guess":
    
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 9: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print ("you guessed it!")
        break"""
    
#Method Two
num = random.randint(1,9)
print("Wellcome to the Guess Me Game.")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guess = [0]

#use while loop
"""while True:
    user_num = int(input("What is your guess :"))
    if (user_num < 1 or user_num >9):
        print("Out Of Bound")
        continue
    elif(user_num < num):
        print("Your guess Number is low")
        continue
    elif(user_num > num):
        print("Your guess Number is high")
    else:
        print(f'Contratulation.You take {len(guess)}')
        break
        guess.append(user_num)"""
