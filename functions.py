import constants
from ship import Ship


# Clears the screen
def clear_screen():
    print("\033c", end="")


# Prints the board heading
def print_board_heading():
    print("   " + " ".join([chr(c)
          for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)]))


# Prints the board
def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


# Checks if an entire fleet is sunk
def check_fleet(fleet):
    # import pdb; pdb.set_trace()
    for boat in fleet:
        if not boat.is_sunk():
            return False
    return True


# Main game loop
def my_turn(player_turn, player_opposition):
    error_message = ""
    while True:
        # 10. Display boards to the screen.
        clear_screen()
        player_turn.my_shots_board.display()
        player_turn.my_ships_board.display()

        # Display results
        if error_message.strip() != "":
            print(error_message + '\n')

        # 11. Prompt player for guess.
        position = input("{}, Enter a location: ".format(player_turn))
        postion_tuple = valid_position(position.strip())
        # 12. Validate guess.
        if not postion_tuple:
            error_message = ("Your entry was not valid. Please try again, "
                             "for example a1 is the top left position.")
            continue

        # Check if tried this position already
        if player_turn.my_shots_board.ship_exists(postion_tuple):
            error_message = ("You have already tryed the position {}. "
                             "Please try a new position."
                             .format(position.upper()))
            continue

        # If we get here, the entry was vaild, so beak out
        break

    # 13. Display guess results.
    # Default is that you missed
    message = "Sorry {}, your shot missed.\n".format(player_turn)
    player_turn.my_shots_board.hit_or_miss(postion_tuple, False)

    # Now check if it was actually a hit
    for ship in player_opposition.my_fleet:
        if ship.is_hit(postion_tuple):
            message = "*** IT'S  A  HIT ***\n"

            # Mark the hit on player my_shots and opposition my_ships board
            player_turn.my_shots_board.hit_or_miss(postion_tuple)
            player_opposition.my_ships_board.hit_or_miss(postion_tuple)

            # Check and mark if the ship is sunk
            if ship.is_sunk():
                player_turn.my_shots_board.sunk(ship)
                player_opposition.my_ships_board.sunk(ship)
                message = message + ("Well done, you have sunk {}'s {}\n"
                                     .format(player_opposition, ship.model))

                # Check if the whole fleet is sunk
                if check_fleet(player_opposition.my_fleet):
                    message = (message + "All of {}'s ships have been sunk! "
                               "{} is the winner!\n"
                               .format(player_opposition, player_turn))
                    break
                else:
                    break
            else:
                break

    return message


# Place the ships on the players board, prompting for and validating position.
def place_ships(board):
    ships_list = []
    for ship in constants.SHIP_INFO:
        error_message = ""
        while True:
            # Clear the screen
            clear_screen()

            # Display the board
            board.display()

            # Display the error message if there is one
            if error_message.strip() != "":
                print(error_message + '\n')

            # Get the user input§
            position = input("Place the location of the {} ({} spaces): "
                             .format(ship[0], ship[1])).strip()

            # Check the input is valid
            postion_tuple = valid_position(position)
            if not postion_tuple:
                error_message = ("Your entry was not valid. Please try again, "
                                 "for example A1 is the top left position.")
                continue

            # Check the start positon is not taken
            if board.ship_exists(postion_tuple):
                error_message = ("There is already a ship at position {}, "
                                 "please try another position."
                                 .format(position.upper()))
                continue

            # Get the orientation of the ship, default h
            orientation = (input("Is it horizontal or vertical? (H)/v: ")
                           .lower().strip())
            if orientation != 'h' and orientation != 'v':
                orientation = 'h'

            # Try to place the ship on the board
            position_list = board.place_ship(
                orientation,
                postion_tuple,
                ship[1])
            if position_list:
                # Create ship
                ships_list.append(Ship(ship[0], position_list))

                # Break loop
                break

            else:
                error_message = ("There is not enough room to place the {} "
                                 "at {}:{}".format(
                                    ship[0],
                                    position.upper(),
                                    orientation.upper()))
                continue

    # Return a dictionary of ships for the board
    return ships_list


# 4. Validate user input.
def valid_position(position):
    """Tests if the entered position is valid
    1. Must be either 'letterNumber' or 'numberLetter'.
    2. Number must be <= BOARD_SIZE
    """
    # Valid position are at least 2 characters
    if len(position) < 2:
        return False

    # 5. Be as accepting as possible of input.
        # Any case
        # Allow letters and numbers to  be put in any order

    # Valid position starts or ends with a letter
    if position[0].lower() in constants.VALID_LETTERS:
        try:
            x = constants.VALID_LETTERS.find(position[0].lower())
            y = int(position[1:]) - 1
            if (x < constants.BOARD_SIZE and
                    y < constants.BOARD_SIZE and y >= 0):
                return x, y
            else:
                return False
        except ValueError:
            return False

    if position[-1].lower() in constants.VALID_LETTERS:
        try:
            x = constants.VALID_LETTERS.find(position[-1].lower())
            y = int(position[:-1]) - 1
            if (x < constants.BOARD_SIZE and
                    y < constants.BOARD_SIZE and y >= 0):
                return x, y
            else:
                return False
        except ValueError:
            return False

    # Not valid so default to return false
    return False
