import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

print(logo + "\n\n")
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)
level = input("Choose a diffculty (easy or hard): ")

attempts = HARD_TURNS if level == 'hard' else EASY_TURNS
print(f"You have {attempts} attempts remaining to guess the number.")
game_over = False

while attempts > 0 and not game_over:
  guess = int(input("\nMake a guess: "))
  if guess > num:
    print("Too high")
  elif guess < num:
    print("Too low")
  else:
    print("You guessed it right!! You WIN!!!")
    game_over = True
  if game_over == False:
    attempts -= 1
    print(f"Guess again\nYou have {attempts} more to guess again.")

if not game_over:
  print(f"You've run out of guesses!!\nThe correct number was {num}")
