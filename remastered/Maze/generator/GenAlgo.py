from abc import ABC, abstractmethod

class GenAlgo(metaclass=ABC):
    def __init__(self,widht, height):
        """
        Maze generator Constructor

        attributes:
        -----------
            h (int): height of maze, in number of hall ways
            w (int): widht of maze, in numuber of hall ways
            H (int): height in hall ways + walls 
            W (int): widht in hall ways + walls
            example: h.w = 2.2, H.W = 5.5
              1 2 3 4 5
            1 1 1 1 1 1
            2 1 0 1 0 1
            3 1 1 1 1 1
            4 1 0 1 0 1
            5 1 1 1 1 1
        """
        
        self.w = widht
        self.h = height
        self.W = widht*2 + 1
        self.height = height*2 + 1

    
    @abstractmethod
    def _get_neighbour(self,grid, r, c, not_visted = True ):
        """ find all neighbor of current cell, visted or not 
        args:
            grid: maze matrix 1 is walls or not visted, 0 is visted or grid space
            r (int): current cells row
            c (int): current cells col
        return: [] of neighbour cells, is visted or not
            """
        
        neighbour = []
        #top
        if r > 1 and grid[r-2][c] ==not_visted:
            neighbour.append((r-2, c))
        if r < self.H-2  and grid[r+2][c] ==not_visted:
            neighbour.append((r+2, c))
        if c > 1  and grid[r][c-2] ==not_visted:
            neighbour.append((r, c-2))
        if c <self.W -2 and grid[r][c-2] ==not_visted:
            neighbour.append((r, c+2))

        return neighbour


        





        

