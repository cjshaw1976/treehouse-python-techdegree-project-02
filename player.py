class Player():
    """Defines the player. Each player has
    a name (string)
    a board to place thier ships (board)
    a board to display thier shots (board)
    a fleet (list of ships)
    """

    my_ships_board = ""
    my_shots_board = ""
    my_fleet = ""

    def __init__(self, player_number=1):
        """Instantizes the player.
        Takes a integer representing the player number.
        Prompts for a player name.
        """
        self.player_number = player_number

        # Loop till we get a non white space name
        while True:
            name = input("Player {} Name > ".format(self.player_number))
            if not name.strip():
                print("Invalid Name. Please try again.\n")
            else:
                break

        self.name = name.strip()
        print("Welcome {}. Thank you for joining the battle.\n"
              .format(self.name))

    def __str__(self):
        """Returns the player name"""
        return self.name
