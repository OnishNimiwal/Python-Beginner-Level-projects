import random

def guess(x):
    low =1
    high =x
    feedback= ''
    cnt = 0
    while feedback!='c':
        if (low!=high):
            guess = random.randint(low, high)
        else:
            guess = low = high
        feedback= input(f"Is {guess} is too high (H), Is {guess} is too low (L) or correct (C) ").lower()
        cnt += 1
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1
        else:
            print(f"🎉 Congrats! I guessed the number {guess} in {cnt} tries.")
            break

if __name__ == "__main__":
    print("Enter the No which you want ot computer to guess:")
    num = int(input("Enter No: "))
    guess(num)
