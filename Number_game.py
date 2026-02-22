from random import randrange

def score(count, y):
    left_attempt = y - count
    return (left_attempt/y)*100

def play_game():
    x = randrange(1, 101)

    count = 0
    while True:
        difficulty = input("Chose the difficulty of the game (Hard/Medium/Easy)").lower()
        if difficulty == 'hard':
            print("In Hard Difficulty you will get 10 attempts. \nLet's Begun")
            y = 10
            break
        elif difficulty == 'medium':
            print("In Medium Difficulty you will get 15 attempts. \nLet's Begun")
            y = 15
            break
        elif difficulty == 'easy':
            print("In Easy Difficulty you will get 20 attempts. \nLet's Begun")
            y =  20
            break
        else:
            print("Enter a valid difficulty level.")

    while count < y:
        try:
            guess = int(input("Enter your guessed Number between 1-100: "))
            if 1 <= guess <= 100:
                count += 1
                if guess == x:
                    final_score = round(score(count, y), 2)
                    return f"Congratulation, You have guessed the correct number in {count} turns. So your score is {final_score}%"
                elif guess < x:
                    print("Too Low")
                    print(f"Attempt left for you to guess: {y-count}")
                else:
                    print("Too High")
                    print(f"Attempt left for you to guess: {y - count}")
            else:
                print("Out of Range. Enter a number in range between 1 - 100")
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

    else:
        return (f"You Lost, correct Number was {x}")


while True:
    play = input("Do you want to play a number gussing game?: ").lower()
    if play in ('yes', 'y'):
        print(play_game())
    elif play in ('no', 'n'):
        print("See You Soon")
        break
    else:
        print("Enter a valid Input")