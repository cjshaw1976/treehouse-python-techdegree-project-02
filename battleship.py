import constants
import functions
from board import Board
from player import Player

functions.clear_screen()

# 1. Prompt the players for their names.
player1 = Player(1)
player2 = Player(2)

# 2. Display an empty board.
functions.clear_screen()
input("{}, it is time to set up your ships. Make sure {} is "
      "not looking and press Enter."
      .format(player1, player2))
player1.my_ships_board = Board()
player1.my_shots_board = Board()
player1.my_fleet = functions.place_ships(player1.my_ships_board)

# 8. Prompt second player to place their ships
functions.clear_screen()
input("{} has placed thier fleet. Press Enter for {} to set up thier fleet."
      .format(player1, player2))
player2.my_ships_board = Board()
player2.my_shots_board = Board()
player2.my_fleet = functions.place_ships(player2.my_ships_board)

# 9. Allow players to take turns.
# Main game loop
players = (player2, player1)
while True:
    # Swop the players order each turn
    players = (players[1], players[0])

    # Player has its turn
    message = functions.my_turn(players[0], players[1])

    # Display the results of the turn taken
    functions.clear_screen()
    print(message)

    # At end of game, Display boards and break out of loop
    if "winner" in message:
        print(players[1].name + "'s board")
        players[1].my_ships_board.display()
        print(players[0].name + "'s board")
        players[0].my_ships_board.display()
        break
    else:
        input("{}, it is your turn now. Press Enter when you are ready."
              .format(players[1]))
