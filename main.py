#pbl1: Chloé, Sarah, Nour, Clara
import tkinter as tk 

from board.board_view import Board 

from ai.ai import best_move 

 
# ====================== 

# CONFIGURATION 

# ====================== 

AI_LEVELS = { 

    "Facile": 1, 

    "Moyen": 3, 

    "Difficile (Imbattable)": 9 

} 


# APPLICATION 

class TicTacToeApp: 

    def __init__(self, root): 

        self.root = root 

        self.root.title("Morpion") 

 

        self.board = Board() 

        self.current = "X" 

        self.vs_ai = False 

        self.ai_depth = None 

 

        self.menu_screen() 
=======

 
# START GAME 
    def start_pvp(self): 
        self.vs_ai = False 
        self.start_game() 
 
    def start_ai(self, level): 
        self.vs_ai = True 
        self.ai_depth = AI_LEVELS[level] 
        self.start_game() 
 
    def start_game(self): 
        self.board.reset() 
        self.current = "X" 
        self.clear() 
 
        self.buttons = [] 
        frame = tk.Frame(self.root) 
        frame.pack() 
 
        for i in range(9): 
            btn = tk.Button(frame, text=" ", font=("Arial", 24), 
                            width=5, height=2, 
                            command=lambda i=i: self.play(i)) 
            btn.grid(row=i//3, column=i%3) 
            self.buttons.append(btn) 
 
        self.status = tk.Label(self.root, text="Tour : X", font=("Arial", 14)) 
        self.status.pack(pady=10)
     
#   GAME LOGIC 

    def play(self, index): 

        if self.board.grid[index] != " ": 

            return 

 

        self.board.play(index, self.current) 

        self.buttons[index].config(text=self.current) 

 

        winner = self.board.winner() 

        if winner or self.board.is_full(): 

            self.end_game(winner) 

            return 

 

        self.current = "O" if self.current == "X" else "X" 

        self.status.config(text=f"Tour : {self.current}") 

 

        if self.vs_ai and self.current == "O": 

            self.root.after(300, self.ai_turn) 

 

    def ai_turn(self): 

        move = best_move(self.board, self.ai_depth, "O", "X") 

        self.play(move) 

 

    def end_game(self, winner): 

        if winner: 

            self.status.config(text=f"{winner} a gagné !") 

        else: 

            self.status.config(text="Match nul") 

 

        tk.Button(self.root, text="Menu", command=self.menu_screen).pack(pady=10) 

#  LANCEMENT 
if __name__ == "__main__": 
    root = tk.Tk() 
    app = TicTacToeApp(root) 
    root.mainloop() 
