import random
T = True
while T == True:
    possible_actions = ['R', 'P', 'S']
    computer_actions = random.choice(possible_actions)
    print('The game is about to begin...')
    print('Welcome to Rock, Paper or Scissors game')
    print('enter R for rock, P for paper, or S for scissors')
    user_action = input('enter a choice (R, P, or S): ')
    for i in user_action:
        if i in possible_actions:
            break
    if i not in possible_actions:
        print('value entered is not valid, Please enter R, P, or S')
        continue
    print(f"\nPlayer {user_action} : CPU {computer_actions}.\n")

    if user_action == computer_actions:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_actions == "S":
            print("Rock smashes scissors!, You win!")
        else:
            print("Paper covers rock!, Computer wins.")
    elif user_action == "P":
        if computer_actions == "R":
            print("Paper covers rock!, You win!")
        else:
            print("Scissors cuts paper!, Computer wins.")
    elif user_action == "S":
        if computer_actions == "P":
            print("Scissors cuts paper!, You win!")
        else:
            print("Rock smashes scissors!, Computer wins.")
    
    play_again = input("Do You want to play again? (y/n): ")
    if play_again.lower() == 'y':
        continue
    else:
        print('Thanks for Playing!!, See you next time.')
        break
