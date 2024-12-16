# import random module to generate 2 random people from game_data
import random
# import game-data to use
from game_data import data
# import logo
from art import logo, vs

# A vs B
# logo here
# Compare A Structure: {name}, {description}, from {country}.
# versus logo here
# Against B Structure: {name}, {description}, from {country}.
# User input: 'Who has more followers? A or B': 
# Compare A's followers against B's followers
# If user guesses correctly, it should +1 score and A becomes B or stays A if the choice was A
# If user guesses wrong, game ends

def format_data(person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"

def compare(user_guess, a_person, b_person):
    """ TAKE THE USER'S GUESS AND PERSON A AND PERSON B'S FOLLOWER COUNTS AND COMPARE THEM. Also checks if the user got the guess correctly. """
    # first compares follower counts, then it will return true or false if the user's guess matches
    if a_person > b_person:
        return user_guess == "a"
    else:
        return user_guess == "b"

# when the while loop starts, it will start with these, but if the while loop keeps running, it won't look at it again
game_over = False
score = 0

second_person = random.choice(data)

while not game_over:
    print(logo)
    # FIRST STEP: GET 2 RANDOM PEOPLE FROM GAME DATA
    # make the 2nd person become the next account at 1st person's
    first_person = second_person
    second_person = random.choice(data)



    # SECOND STEP: GET THEIR FOLLOWER COUNTS
    first_person_followers = first_person["follower_count"]
    second_person_followers = second_person["follower_count"]

    # THIRD STEP: COMPARE THEIR FOLLOWER COUNTS TO EACH OTHER, USE A FUNCTION
    print(f"{format_data(first_person)}")
    print(vs)
    print(f"{format_data(second_person)}")

    # FOURTH STEP: Ask the user who has more followers? A or B
    guess = input("Who has more followers? A or B: ").lower()

    # Need to see if the user guess correctly
    is_correct = compare(guess, first_person_followers, second_person_followers)

    # check if the user's guess was correct, add +1 if it was, if not then display final score
    if is_correct:
        score += 1
        print(f"You were right! Score: {score}")
    else:
        # if the user guesses incorrectly, should end the game and also print the final score
        game_over = True
        print(f"You got it wrong.. Final score: {score}")
    
    # IF THE USER GUESSED CORRECTLY, +1 SCORE, OTHERWISE GAME ENDS (need a while loop eventually)