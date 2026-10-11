import random

print("----------- Welcome to Guessing Numbers ------------")

best_score = 0
play_again = "y"

while play_again == "y":
    print("Choose Level")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")
    level = input("Enter level (1/2/3): ")

    if level == "2":
        max_num = 50
    elif level == "3":
        max_num = 100
    else:
        max_num = 10

    score = 0

    for i in range(3):
        r_n = random.randint(1, max_num)
        print("Round", i + 1)

        for attempt in range(1, 6):
            try:
                guess_num = int(input("Guess the Number (1 to " + str(max_num) + "):"))
            except ValueError:
                print("Please enter only number")
                continue

            if guess_num == r_n:
                print("Congratulation..! You Win")
                score += 6 - attempt
                break
            elif guess_num > r_n:
                print("Too High")
            else:
                print("Too Low")
        else:
            print("You Lose")
            print("Number was", r_n)

    print("Score:", score)

    if score > best_score:
        best_score = score
        print("New High Score!")
    print("Best Score:", best_score)

    play_again = input("Play again? (y/n):").lower()

print("Thank you for playing")

