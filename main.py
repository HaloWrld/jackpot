#import random

#Multiple Players able to Play

num_players = int(input("How many people are playing? "))
print(f"Welcome to the Powerball Jackpot! There are {num_players} players.")
while num_players <= 0:
  print("Invalid number of players")
  num_players = int(input("How many people are playing? "))
    

#The first 5 numbers the players guess will be between 0-69 and the sixth number(Powerball Number) will be from 1-26
# for num in range(0,70):
#   while True:
#     user_choice = input("Enter five numbers between (1,69):")
#     random_numbers = random.sample(range(0,70), 5)
#     computer_randomize = random.choice(random_numbers,)
#     print(f"\nYour 5 white ball numbers are {user_choice}, Computers 5 white ball numbers are {computer_randomize}.\n")

#   for num in range(0,27):
#     while True:
#       user_choice = input("Enter One numbers (1,26):")
#       random_numbers = random.sample(range(0,27), 5)
#       computer_randomize = random.choice(random_numbers)
#     print(f"\nYour Red Powerball Number is {user_choice}, The Computers Red Powerball Number is {computer_randomize}.\n")

#Concept of Computer Generating 5 numbers in a list between 0-69 after the players entered there 5 random numbers
    #def generate_number():

#If they win, they will win the jackpot.
#if user_choice == computer_randomize:
  #print(f"Both entered five numbers {user_choice}. You Won!")