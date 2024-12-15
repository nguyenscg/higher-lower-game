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

# get 2 random people from game_data
person1 = random.choice(data)
person2 = random.choice(data)

# get person1's follower_count and get person2's follower_count
print(person1["follower_count"])
print(person2["follower_count"])