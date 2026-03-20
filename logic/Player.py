from logic.Character import Character
class Player(Character):
    def __init__(self, starting_r, starting_c):
        super(Player, self).__init__(starting_r, starting_c)
    
    def win_condition(self, exit_position):
        """ method to check win condition 
        Args:
            exit_position (tuple): (exit_r, exit_c) 
        Returns:
            return (bool): True if player is at the exit
        """
        return (self.r, self.c) == exit_position
    


        