import random

# List to hold the scores
attempt_lists = []

# ANSI escape codes for colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'  # Reset to default color

def show_score():
    if len(attempt_lists) <= 0:
        print(f"{RED}THERE'S NO HIGH SCORE!{RESET}")
    else:
        # Display the highest score in green
        high_score = max(attempt_lists)
        print(f"{GREEN}The highest score is: {high_score}{RESET}")

# Example function to add a score to attempt_lists (for demonstration purposes)
def add_score():
    score = random.randint(1, 100)  # Generate a random score between 1 and 100
    attempt_lists.append(score)
    print(f"{YELLOW}Score {score} added!{RESET}")

# Adding some scores and showing the high score
add_score()
add_score()
show_score()
