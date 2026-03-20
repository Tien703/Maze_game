from generator.GenAlgo import GenAlgo
import random
import numpy as np
class Randomized_DFS(GenAlgo):
    """
    Randomized_DFS algorithm to generate maze
    1.Choose a random starting cell
    2.Select a random neigbouring cell has not visted
        Add path and remove wall between 
        Mark as visted
    3.When at a dead-end it backtracks till a cells with unvisted neigbour
    """
    def __init__(self, w,h):
        super(Randomized_DFS, self).__init__(w,h)
    def generate(self):
        """ Methods to implements Maze generating-algorithm 
        Args: 

        Returns:
            Matrix
        """
        #Create grid full of 1
        grid = np.empty((self.W, self.H),dtype=np.int8)
        grid.fill(1)
        #Pick random cell
        current_row, current_col, = (random.randrange(1, self.W, 2), random.randrange(1, self.H,2)) 
        grid[current_row][current_col] = 0
        track = [(current_row,current_col)]
        path = [(current_row,current_col)]
        #while having cells still have neighbours, visit all neighbour
        while track:
            (crow, ccol) = track[-1]
            neighbors = self._find_neighbors(crow, ccol, grid, True)

            if len(neighbors) == 0:
                track = track[:-1]
            else:
                nrow, ncol = random.choice(neighbors)
                grid[nrow][ncol] = 0
                grid[(nrow + crow) // 2][(ncol + ccol) // 2] = 0

                track += [(nrow, ncol)]
                path += [(nrow, ncol)]
        return grid, path
        
        

    


