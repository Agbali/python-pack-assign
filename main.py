import random


while True:
    list_moves = ["R", "P", "S"]
    
    user_actions = input("'R' for Rock, 'P' for Paper, 'S' for Scissors and 'E' to End game: \n")
    computer_action = random.choice(list_moves)

    if user_actions == "E":
            print("The game has ended")
            break

    elif computer_action == user_actions:
            print("It's a tie! Play again!", "Player:", user_actions, "CPU: ", computer_action)

    elif user_actions == "R": 
        if computer_action == "P":
            print("You lose!", "Player:", user_actions, "CPU: ", computer_action)
            break
        else:
            print("You win!", "Player:", user_actions, "CPU: ", computer_action)
            break
    elif user_actions == "P": 
        if computer_action == "S":
            print("You lose!", "Player:", user_actions, "CPU: ", computer_action)
            break
        else:
            print("You win!", "Player:", user_actions, "CPU: ", computer_action)
            break
    elif user_actions == "S": 
        if computer_action == "R":
            print("You lose!", "Player:", user_actions, "CPU: ", computer_action)
            break
        else:
            print("You win!", "Player:", user_actions, "CPU: ", computer_action)
            break
    else:
        print("Check your input")
   
    
           
                


