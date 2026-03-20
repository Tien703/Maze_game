from abc import ABC
class Object(ABC):
    """ ABC class to define object on maze
            exit_point
            safe_zone
        
    """
    def __init__(self, r, c):
        """ initial Object
            r: object' current row
            c: object' current col
        """
        self.r_position = r
        self.c_postiokn = c
    

