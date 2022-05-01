import random

num_stones = 0
turn = 1 # (1 => Player 1), (2 => Player 2), (3 => Computer)
is_game_over = False
wants_to_play_again = True
num_stones = int(input("Enter the initial number of stones to start the game: ")) 
num_picked_stones = 0

while is_game_over == False and wants_to_play_again == True:
    print(f"Stones remaining: {num_stones}")
    if turn == 1:
        print("-------------------- Player 1's Turn --------------------")
        num_picked_stones=int(input("Enter number of stones to pick (1, 2, or 3): "))
        num_stones -= num_picked_stones 
        if num_stones <= 0:
            is_game_over = True
            print("----- Player 1 won the game -----")
        turn = 2
    elif turn == 2:
        print("-------------------- Player 2's Turn --------------------")
        num_picked_stones=int(input("Enter number of stones to pick (1, 2, or 3): "))
        num_stones -= num_picked_stones 
        if num_stones <= 0:
            is_game_over = True
            print("----- Player 2 won the game -----")
        turn = 3
    else:
        print("-------------------- Computer's Turn --------------------")
        num_picked_stones= random.randint(1, 3) # either 1, 2, or 3
        num_stones -= num_picked_stones 
        print(f"Computer chose {num_picked_stones} stones.")
        if num_stones <= 0:
            is_game_over = True
            print("----- Computer won the game -----")
        turn = 1
    if is_game_over:
        choice=input("Enter yes or (y) to play again, no or (n) to exit: ")
        if choice.lower() in ["y", "yes"]:
            wants_to_play_again = True
            is_game_over = False
            num_stones = int(input("Enter the initial number of stones to start the game: ")) 
        else:
            print("----------------- Game Ended, Thank you for playing! --------------")
        