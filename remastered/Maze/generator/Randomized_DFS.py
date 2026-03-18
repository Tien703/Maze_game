from GenAlgo import GenAlgo
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
        current_row, current_col, = (random.randint(0, self.W), random.ranint(0, self.H)) 
        grid[current_row][current_col] = 0
        



       








    


    
