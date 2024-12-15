# import random module to generate 2 random people from game_data
import random
# import game-data to use
from game_data import data
# import logo
from art import logo

# A vs B
# logo here
# Compare A Structure: {name}, {description}, from {country}.
# versus logo here
# Against B Structure: {name}, {description}, from {country}.
# User input: 'Who has more followers? A or B': 
# Compare A's followers against B's followers
# If user guesses correctly, it should +1 score and A becomes B or stays A if the choice was A
# If user guesses wrong, game ends

# FIRST STEP: GET 2 RANDOM PEOPLE FROM GAME DATA
first_person = random.choice(data)
second_person = random.choice(data)
print(first_person)
print(second_person)