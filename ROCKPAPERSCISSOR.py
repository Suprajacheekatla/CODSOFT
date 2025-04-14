import random
from colorama import Fore, Style, init
import time
init(autoreset=True)

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Function to get emoji for choice
def get_choice_emoji(choice):
    return {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }.get(choice, '')

# Fancy print with delay for style
def stylish_print(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    print(Fore.CYAN + Style.BRIGHT + """
╔══════════════════════════════════════╗
║    🎮 Welcome to Rock-Paper-Scissors 🎮    ║
╚══════════════════════════════════════╝
""")

    while True:
        stylish_print("\nChoose one: rock, paper, or scissors.", Fore.YELLOW)
        user_choice = input(Fore.GREEN + "Your choice 👉 : ").lower()

        while user_choice not in ['rock', 'paper', 'scissors']:
            stylish_print("Oops! Invalid input. Please choose rock, paper, or scissors.", Fore.RED)
            user_choice = input(Fore.GREEN + "Your choice 👉 : ").lower()

        computer_choice = get_computer_choice()

        stylish_print(f"\n🧍 You chose: {user_choice} {get_choice_emoji(user_choice)}", Fore.BLUE)
        time.sleep(0.5)
        stylish_print(f"🤖 Computer chose: {computer_choice} {get_choice_emoji(computer_choice)}", Fore.MAGENTA)
        time.sleep(0.5)

        result = determine_winner(user_choice, computer_choice)

        if result == 'tie':
            stylish_print("It's a tie! 😐", Fore.YELLOW)
        elif result == 'user':
            stylish_print("You win this round! 🎉", Fore.GREEN)
            user_score += 1
        else:
            stylish_print("You lose this round! 💔", Fore.RED)
            computer_score += 1

        stylish_print(f"\n📊 Scoreboard ➤ You: {user_score} | Computer: {computer_score}", Fore.CYAN)
        print(Fore.LIGHTBLACK_EX + "────────────────────────────────────────")

        play_again = input(Fore.YELLOW + "Play another round? (yes/no): ").lower()
        if play_again != 'yes':
            stylish_print("\nThanks for playing! 👋 Stay awesome!", Fore.CYAN)
            stylish_print("Made with ❤️ in Python", Fore.MAGENTA)
            break

# Start the game
play_game()
