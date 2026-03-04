#pbl1: Chloé, Sarah, Nour, Clara
import tkinter as tk 
from Board.board import Board 
from AI.ai import best_move  

# CONFIGURATION  

AI_LEVELS = { 
    "Easy": 1, 
    "Medium": 3, 
    "Hard": 9 
} 


# APPLICATION 

class TicTacToeApp: 
    
    def __init__(self, root): 
        self.root = root 
        self.root.title("Tic Tac Toe") 
        self.root.geometry("500x500")
        self.root.resizable(False,False)
        self.root.configure(bg = "#B8DFFF")

        self.board = Board() 
        self.current = "X" 
        self.vs_ai = False 
        self.ai_vs_ai = False
        self.ai_depth = None 

        self.menu_screen() 

# INTERFACE
    def clear(self): #to clear the window 
        for widget in self.root.winfo_children(): 
            widget.destroy() 

    def menu_screen (self):
        self.clear() #tomake sure the window is empty before adding widgets
        tk.Label(
            self.root, 
            text="TIC TAC TOE", 
            font=("Arial Rounded MT Bold", 50, "bold"),
            bg = "#B8DFFF"
        ).pack(pady=15) #title + font + places it on the window
        tk.Button(
            self.root, 
            text="Player vs Player", 
            width = 18,
            height = 2,
            font = ("Arial Rounded MT Bold", 30),
            bg = "#FFB3DA",
            command=self.start_pvp
        ).pack(pady=15) #creates buttons for the two possibilities #command = what happens when you click the button
        tk.Button(
            self.root, 
            text="Player vs AI", 
            width = 18,
            height = 2,
            font = ("Arial Rounded MT Bold", 30),
            bg = "#E0B3FF",
            command=self.ai_menu
        ).pack(pady=15) 
        tk.Button(
            self.root, 
            text="AI vs AI", 
            width = 18,
            height = 2,
            font = ("Arial Rounded MT Bold", 30),
            bg = "#D8C4FF",
            command=self.ai_menu
        ).pack(pady=15)

    def ai_menu(self):
        self.clear() 
        tk.Label(self.root, text="Choose a difficulty level", font=("Arial Rounded MT Bold", 30), bg = "#B8DFFF").pack(pady=10) 
 
        for level in AI_LEVELS: 
            tk.Button(
                self.root, 
                text = level, 
                width = 15,
                height = 2,
                font = ("Arial Rounded MT Bold", 20),
                bg = "#FFB3DA",
                command=lambda l=level: self.start_ai(l)
            ).pack(pady=10) #creates a button for difficulty and start this difficulty #lambda function to remember the right level 
        tk.Button(
            self.root,
            text="Back to menu",
            font = ("Arial Rounded MT Bold", 20),
            bg = "#D8C4FF",
            command=self.menu_screen
        ).pack(pady=10) 

 
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
        frame = tk.Frame(self.root,bg = "#B8DFFF") 
        frame.pack(pady = 50) 
 
        for i in range(9): 
            btn = tk.Button(frame, text=" ", font=("Arial Rounded MT Bold", 24), 
                            width=5, height=2, 
                            command=lambda i=i: self.play(i)) 
            btn.grid(row=i//3, column=i%3) 
            self.buttons.append(btn) 
 
        self.status = tk.Label(self.root, text="Turn : X", font=("Arial Rounded MT Bold", 14), bg = "#B8DFFF") 
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
            self.status.config(text=f"{winner} won !") 

        else: 
            self.status.config(text="It's a tie") 

        tk.Button(self.root, text="Menu", command=self.menu_screen).pack(pady=10) 

#  LANCEMENT 
if __name__ == "__main__": 
    root = tk.Tk() 
    app = TicTacToeApp(root) 
    root.mainloop() 
