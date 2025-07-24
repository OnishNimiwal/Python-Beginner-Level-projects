import random

def guess(x, y):
    random_number = random.randint(x, y)
    cnt = 0
    while True:
        num = int(input("Enter your guess: "))
        cnt += 1
        if num < random_number:
            print("Guess a higher number.")
        elif num > random_number:
            print("Guess a lower number.")
        else:
            print(f"🎉 Congrats! You guessed the number in {cnt} tries.")
            break

if __name__ == "__main__":
    print("Enter the range to generate the random number:")
    num1 = int(input("From number 1: "))
    num2 = int(input("To number 2: "))
    guess(num1, num2)
