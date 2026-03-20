from logic.config import DIRECTION_MAP
from abc import ABC
class Character(ABC):
    """ abtraction class for players and ghosts
    """
    def __init__(self, starting_r, starting_c):
        self.r = starting_r 
        self.c = starting_c

    def moves(self,direction):
        """Method to move character around
        Args: 
            direction (int): 1: up, 2: down, 3:left, 4:right
        Returns
            player.r, player.c
        """
        dx, dy = DIRECTION_MAP[direction]
        self.r += dx
        self.c += dy
    def valid_direction(self, grid, direction):
        """ Method to check valid move
        Args: 
            grid (numpy.ndarray): The maze grid
            direction (int): 1: up, 2: down, 3: left, 4: right
        Returns
            Valid? (bool): True if the move is within boundaries and not a wall (0 is path, 1 is wall)
        """
        dr, dc = DIRECTION_MAP[direction]
        new_r, new_c = self.r + dr, self.c + dc
        
        # Check boundaries
        if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])):
            return False
            
        # Check if it's a wall (1 is wall, 0 is path)
        if grid[new_r][new_c] == 1:
            return False
            
        # Also check the cell in between for wall
        mid_r, mid_c = self.r + dr // 2, self.c + dc // 2
        if grid[mid_r][mid_c] == 1:
            return False

        return True


         

