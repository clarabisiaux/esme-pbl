def evaluate(board, ai_symbol, human_symbol): #score to know who the winner is
  winner=board.winner()
  if winner == ai_symbol:
    return 10
  elif winner == human_symbol:
    return -10
  return 0
  

def minimax(board, depth, maximizing, ai_symbol, human_symbol): #recursive function
  score = evaluate(board, ai_symbol, human_symbol)

  if score != 0 or board.is_full() or depth==0: #if end of game
    return score

  if maximizing: #AI turn
    best = -1000
    for move in board.available_moves():
      board.grid[move] = ai_symbol
      best = min(best, minimax(board, depth-1, False, ai_symbol, human_symbol))
      board.grid[move] = " "
    return best

  else: #player turn
    best = 1000
    for move in board.available_moves():
      board.grid[move] = human_symbol
      best = min(best, minimax(board, depth-1, True, ai_symbol, human_symbol))
      board.grid[move] = " "
    return best

def best_move(board, depth, ai_symbol, human_symbol):
  best_score = -1000
  move_choice = None
  
  for move in board.available_moves(): #try all the possible moves
    board.grid[move] = ai_symbol
    score = minimax(board, depth-1, False, ai_symbol, human_symbol) #score for each move
    board.grid[move] = " "
    if score>best_score: #keep the best score
      best_score = score
      move_choice = move
      
    return move_choice


