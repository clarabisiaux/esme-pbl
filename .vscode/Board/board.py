class Board: 

    def __init__(self): 

        self.grid = [" " for _ in range(9)] 

 

    def play(self, index, symbol): 

        if self.grid[index] == " ": 

            self.grid[index] = symbol 

            return True 

        return False 

 

    def available_moves(self): 

        return [i for i in range(9) if self.grid[i] == " "] 

 

    def is_full(self): 

        return " " not in self.grid 

 

    def winner(self): 

        lines = [ 

            (0,1,2),(3,4,5),(6,7,8), 

            (0,3,6),(1,4,7),(2,5,8), 

            (0,4,8),(2,4,6) 

        ] 

        for a, b, c in lines: 

            if self.grid[a] == self.grid[b] == self.grid[c] != " ": 

                return self.grid[a] 

        return None 

 

    def reset(self): 

        self.grid = [" " for _ in range(9)] 
        
