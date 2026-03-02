class Board: 

    def __init__(self): 
        self.grid = [" " for _ in range(9)] #create 9 empty boxes

    def play(self, index, symbol): #if the box is empty it puts the symbol in it
        if self.grid[index] == " ": 
            self.grid[index] = symbol 
            return True 
        return False #if the box isn't empty you can't play

    def available_moves(self): 
        return [i for i in range(9) if self.grid[i] == " "] #return all the empty boxes (playable boxes)

    def is_full(self): #check if the board is full
        return " " not in self.grid 

    def winner(self): 
        lines = [ 
            (0,1,2),(3,4,5),(6,7,8), 
            (0,3,6),(1,4,7),(2,5,8), 
            (0,4,8),(2,4,6) 
        ] #list of winning combinations

        for a, b, c in lines: 
            if self.grid[a] == self.grid[b] == self.grid[c] != " ": #if abc is the same symbol and not empty and part of the winning combinations
                return self.grid[a] #return the winning symbol (the winner)
        return None #if there is no winning lines no one wone

    def reset(self): #recreate an empty grid to restart
        self.grid = [" " for _ in range(9)] 
        
