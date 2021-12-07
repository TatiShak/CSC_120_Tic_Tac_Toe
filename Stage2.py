def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Select a cell, for this enter a number from 1-9 " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Incorrect entry. Do you need to enter a number between 1-9?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("The cell is busy")
        else:
            print ("Incorrect entry. Enter a number from 1 to 9")

