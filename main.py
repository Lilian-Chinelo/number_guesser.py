import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
###### Difficulty level #########
if difficulty == "easy":
  print("You have 10 attempts to guess the number.")
elif difficulty == "hard":
  print("You have 5 attempts to guess the number.")
else:
  print("Please type 'easy' or 'hard'.")

### Generate a random number once in the guessing cycle between the range. ###
number_of_choice = random.randint(1, 101)

###The function ###
def number_guesser():
  guess_again = True
  turns_left_hard = 5
  turns_left_easy = 10
  user_guess = int(input("Make a guess: "))
  
  while guess_again:
    
    # print(number_of_choice)
    if user_guess > number_of_choice:
      if difficulty == "easy":
        print("Too high.")
        if turns_left_easy > 0:
          turns_left_easy -= 1
          print(f"You have {turns_left_easy} attempts left to guess the number.")
          user_guess = int(input("Make a guess: "))
        else:
          print(f"You lost!, the correct number is {number_of_choice}")
          guess_again = False
          break
      elif difficulty == "hard":
        print("Too high.")
        if turns_left_hard > 0:
          turns_left_hard -= 1
          print(f"You have {turns_left_hard} attempts left to guess the number.")
          user_guess = int(input("Make a guess: "))
        else:
          print(f"You lost!, the correct number is {number_of_choice}")
          guess_again = False
          break
    elif user_guess < number_of_choice:
      if difficulty == "easy":
        print("Too low.")
        if turns_left_easy > 0:
          turns_left_easy -= 1
          print(f"You have {turns_left_easy} attempts left to guess the number.")
          user_guess = int(input("Make a guess: "))
        else:
          print(f"You lost!, the correct number is {number_of_choice}")
          guess_again = False
          break
      elif difficulty == "hard":
        print("Too low.")
        if turns_left_hard > 0:
          turns_left_hard -= 1
          print(f"You have {turns_left_hard} attempts left to guess the number.")
          user_guess = int(input("Make a guess: "))
        else:
          print(f"You lost!, the correct number is {number_of_choice}")
          guess_again = False
          break
    elif user_guess == number_of_choice:
      print(f"You guessed it right!, the correct number is {number_of_choice} you win!")
      guess_again = False
 
number_guesser()