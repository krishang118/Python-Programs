import random
snakes = {41:20, 59:37, 82:61, 99:4, 67:50, 31:14, 92:76}
ladders = {2:23, 39:80, 62:78, 17:93, 75:96, 29:54, 32:51, 8:12}
def rollingdice():
    return random.randint(1, 6)
def moveingplayer(player, steps):
    player += steps
    if player in snakes:
        print("Ah! A snake bit you! Move back to", snakes[player],".")
        player = snakes[player]
    elif player in ladders:
        print("Wow! You got a ladder! Climb up to", ladders[player],".")
        player = ladders[player]
    return player
def winner(player):
    return player >= 100
def playgame():
    player1 = 0
    player2 = 0
    currentplayer = 1
    while True:
        input("Player {}, press enter to roll the dice...".format(currentplayer))
        diceroll = rollingdice()
        print("Player {} rolled a {}.".format(currentplayer, diceroll))
        if currentplayer == 1:
            player1 = moveingplayer(player1, diceroll)
            print("Player 1 is now at", player1,".\n.")
            if winner(player1):
                print("Congrats to you, Player 1! You're the winner!")
                break
        else:
            player2 = moveingplayer(player2, diceroll)
            print("Player 2 is now at", player2,".\n.")
            if winner(player2):
                print("Congrats to you, Player 2! You're the winner!")
                break
        currentplayer = 3 - currentplayer 
playgame()