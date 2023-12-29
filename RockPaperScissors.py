import random

seq1 = ['Rock', 'Paper', 'Scissors']
seq2 = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


def winorlose(user, computer):
    if user == computer:
        return "It's a tie!"

    if user == 'Paper' and computer == 'Rock':
        return 'You Win! - Paper covers Rock'
    if user == 'Scissors' and computer == 'Paper':
        return 'You Win! - Scissors cut Paper'
    if user == 'Rock' and computer == 'Scissors':
        return 'You Win! - Rock smashes Scissors'

    if user == 'Rock' and computer == 'Paper':
        return 'You Lose! - Paper covers Rock'
    if user == 'Paper' and computer == 'Scissors':
        return 'You Lose! - Scissors cut Paper'
    if user == 'Scissors' and computer == 'Rock':
        return 'You Lose! - Rock smashes Scissors'

    if user == 'Paper' and computer == 'Spock':
        return 'You Win! - Paper disproves Spock'
    if user == 'Rock' and computer == 'Lizard':
        return 'You Win! - Rock crushes Lizard'
    if user == 'Scissors' and computer == 'Lizard':
        return 'You Win! - Scissors decapitate Lizard'
    if user == 'Lizard' and computer == 'Paper':
        return 'You Win! - Lizard eats Paper'
    if user == 'Lizard' and computer == 'Spock':
        return 'You Win! - Lizard poisons Spock'
    if user == 'Spock' and computer == 'Scissors':
        return 'You Win! - Spock smashes Scissors'
    if user == 'Spock' and computer == 'Rock':
        return 'You Win! - Spock vaporizes Rock'

    if user == 'Spock' and computer == 'Paper':
        return 'You Lose! - Paper disproves Spock'
    if user == 'Lizard' and computer == 'Rock':
        return 'You Lose! - Rock crushes Lizard'
    if user == 'Lizard' and computer == 'Scissors':
        return 'You Lose! - Scissors decapitate Lizard'
    if user == 'Paper' and computer == 'Lizard':
        return 'You Lose! - Lizard eats Paper'
    if user == 'Spock' and computer == 'Lizard':
        return 'You Lose! - Lizard poisons Spock'
    if user == 'Scissors' and computer == 'Spock':
        return 'You Lose! - Spock smashes Scissors'
    if user == 'Rock' and computer == 'Spock':
        return 'You Lose! - Spock vaporizes Rock'


if __name__ == '__main__':
    playing = True

    while playing:
        print("1. Rock - Paper - Scissors")
        print("2. Rock - Paper - Scissors - Lizard - Spock")
        mode = None
        while mode not in {"1", "2"}:
            mode = input("Select game mode:")

            if mode not in {"1", "2"}:
                print("Invalid mode, please choose again!")

        if mode == '1':
            print("\nRock, Paper, or Scissors?")
            userchoice = None
            while userchoice not in {"Rock", "Paper", "Scissors"}:
                userchoice = input("Select your move:")

                if userchoice not in {"Rock", "Paper", "Scissors"}:
                    print("Invalid choice, please choose again!")

            computerchoice = random.choice(seq1)

            result = "\n" + winorlose(userchoice, computerchoice)
            print(result)

        elif mode == '2':
            print("\nRock, Paper, Scissors, Lizard, or Spock?")
            userchoice = None
            while userchoice not in {"Rock", "Paper", "Scissors", "Lizard", "Spock"}:
                userchoice = input("Select your move:")

                if userchoice not in {"Rock", "Paper", "Scissors", "Lizard", "Spock"}:
                    print("Invalid choice, please choose again!")

            computerchoice = random.choice(seq2)

            result = "\n" + winorlose(userchoice, computerchoice)
            print(result)

        again = None
        while again not in {"Y", "N"}:
            again = input("\nWould you like to play again? (Y/N)")

            if again not in {"Y", "N"}:
                print("Invalid choice, please choose again!")

        if again == "Y":
            print()

        if again == "N":
            playing = False
