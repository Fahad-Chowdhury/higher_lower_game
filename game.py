from random import choice

from clear_screen import clear
from ascii_art import higher_lower_art, vs_art
from game_data import data


def get_input_from_user():
    ''' Get input from user. It only takes A or B as valid choices. '''
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    while choice not in ['A', 'B']:
        print("Please enter a valid choice: 'A' or 'B'")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return choice


def get_a_random_unique_data(used_options):
    ''' Get a random data from game_data module that has not been fetched
    previously. '''
    choosen_data = choice(data)
    while choosen_data in used_options:
        choosen_data = choice(data)
    return choosen_data


def display_options(option_a, option_b):
    ''' Display the choices for the user. '''
    print(f"\nCompare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.\n")
    print(vs_art)
    print(f"\nAgainst B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.\n")


def check_answer(option_a, option_b, choice):
    ''' Compares followers count of option_a and option_b. It reurns True,
    if choice has the correct winner. '''
    winner = 'A' if option_a['follower_count'] > option_b['follower_count'] else 'B'
    return choice == winner


def display_start_screen():
    ''' Clears the screen and displays higher-lower ascii art. '''
    clear()
    print(higher_lower_art)


def higher_lower_game():
    ''' Main method for executing higher lower game. '''
    used_options = []
    score = 0
    game_over = False

    option_a = None
    option_b = get_a_random_unique_data(used_options)
    used_options.append(option_b)
    display_start_screen()

    while not game_over:
        option_a = option_b
        option_b = get_a_random_unique_data(used_options)
        used_options.append(option_b)
        display_options(option_a, option_b)

        choice = get_input_from_user()
        display_start_screen()

        correct_answer = check_answer(option_a, option_b, choice)       
        if correct_answer:
            score += 1
            print(f"\nYou're right! Current score: {score}\n")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}\n")
            game_over = True


if __name__ == "__main__":
    higher_lower_game()
