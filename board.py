import constants
import functions
import ship


class Board():
    """Defines the playing board. A board contains an equal number of rows and
    colums."""
    def __init__(self):
        """Create a blank board and display it, and populate with ships"""
        self.board = [[constants.EMPTY for num in range(constants.BOARD_SIZE)]
                      for num in range(constants.BOARD_SIZE)]

    # Call to print the board to the screen
    def display(self):
        functions.print_board(self.board)
        print("\n")

    # Mark on board if hit or miss
    def hit_or_miss(self, position, hit=True):
        if hit:
            self.board[position[1]][position[0]] = constants.HIT
        else:
            self.board[position[1]][position[0]] = constants.MISS

    # Mark ship as sunk
    def sunk(self, ship):
        for position in ship.position_list:
            self.board[position[1]][position[0]] = constants.SUNK

    # 6. Validate ship placement.
    def ship_exists(self, position):
        """Tests if the given location is a ship or not"""
        if self.board[position[1]][position[0]] == constants.EMPTY:
            return False
        else:
            return True

    # 7. Update the board.
    def place_ship(self, orientation, position, ship_length):
        # If the ship is going to go off the board,
        # make the start point the end point
        reverse = 1
        if (
                (orientation == 'h' and
                 position[0] + ship_length > constants.BOARD_SIZE) or
                (orientation == 'v' and
                 position[1] + ship_length > constants.BOARD_SIZE)):
            reverse = -1

        if orientation == 'h':
            ship_positions = [(x, position[1]) for x in
                              range(position[0], position[0] +
                              (ship_length * reverse), reverse)]
        else:
            ship_positions = [(position[0], y) for y in
                              range(position[1], position[1] +
                              (ship_length * reverse), reverse)]

        # Check if the position of the ship will overlap other ships
        conflict = False
        for position in ship_positions:
            if self.ship_exists(position):
                conflict = True
                return False

        # Mark the board with the position of the ship and
        # create a list of tuples of the cordinates of the ship
        ship_list = []
        for position in ship_positions:
            ship_list.append((position[0], position[1]))
            if orientation == 'h':
                self.board[position[1]][position[0]] = \
                           constants.HORIZONTAL_SHIP
            else:
                self.board[position[1]][position[0]] = constants.VERTICAL_SHIP

        # Return a list of tuples for the cordinates of the ship
        return ship_list
