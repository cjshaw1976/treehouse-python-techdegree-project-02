import constants


class Ship():
    """Defines the ship. A ship has:
    a model (Name): For reference
    a position list (list of tupples): To show the positions of the ship
    a hits list (list of strings): To show where the ship has been hit
    """

    def __init__(self, model, position_list):
        self.model = model
        self.position_list = position_list
        self.hits_list = [constants.EMPTY for num in range(len(position_list))]

    # Check if ship is hit, and mark the hit
    def is_hit(self, position):
        p = 0
        # import pdb; pdb.set_trace()
        for pos in self.position_list:
            if pos == position:
                self.hits_list[p] = constants.HIT
                return True
            p += 1
        return False

    # Check if ship has been sunk
    def is_sunk(self):
        for hit in self.hits_list:
            if hit == constants.EMPTY:
                return False
        return True
