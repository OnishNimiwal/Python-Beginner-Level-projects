import random

def play():
    user = input("Enter your choice:\nR for Rock\nS for Scissors\nP for Paper\n").upper()
    computer = random.choice(['R', 'S', 'P'])

    if user not in ['R', 'S', 'P']:
        return "Invalid input. Please enter R, S, or P."

    if user == computer:
        return f"Tie! Both chose {user}"
    elif iswin(user, computer):
        return f"You won!!!\nComputer choice: {computer}\nYour choice: {user}"
    else:
        return f"You lose!!!\nComputer choice: {computer}\nYour choice: {user}"

def iswin(player, opponent):
    # Return True if player beats opponent
    return ((player == 'R' and opponent == 'S') or
            (player == 'S' and opponent == 'P') or
            (player == 'P' and opponent == 'R'))

# Call the function and print the result
print(play())
