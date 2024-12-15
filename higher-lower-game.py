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

# check the follower counts against person a versus person b
def compare(a_person, b_person):
    if a_person["follower_count"] > b_person["follower_count"]:
        return a_person
    else:
        return b_person

# get 2 random people from game_data
person1 = random.choice(data)
person2 = random.choice(data)

# get person1's follower_count and get person2's follower_count
# print(person1["follower_count"])
# print(person2["follower_count"])

# compare their follower counts to each other and person b needs to be stored in person a if it's guessed correctly
personA = ""
follower_count1 = person1["follower_count"]
follower_count2 = person2["follower_count"]

# # get user's guess input
# print(person1)
# print("VS.")
# print(person2)
# guess = input("Who has more followers? A or B: ")

# Check user's guess if it's correct


# Keep score, score starts at 0, if user guesses right +1, if not, game ends and restarts