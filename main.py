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

 

# ====================== 

# APPLICATION 

# ====================== 

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
class tictactoe :
    #pbl1
    def __init__(self,couleur):
        self.couleur = couleur

# -------- GAME LOGIC -------- 

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

