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

def compare(a_person, b_person):
    if a_person > b_person:
        print(a_person)
        return a_person
    else:
        print(b_person)
        return b_person

# FIRST STEP: GET 2 RANDOM PEOPLE FROM GAME DATA
first_person = random.choice(data)
second_person = random.choice(data)

# SECOND STEP: GET THEIR FOLLOWER COUNTS
first_person_followers = first_person["follower_count"]
second_person_followers = second_person["follower_count"]

# THIRD STEP: COMPARE THEIR FOLLOWER COUNTS TO EACH OTHER, USE A FUNCTION
print(f"{first_person} versus {second_person}")
compare(first_person_followers, second_person_followers)

# FOURTH STEP: Ask the user who has more followers? A or B
guess = input("Who has more followers? A or B: ")