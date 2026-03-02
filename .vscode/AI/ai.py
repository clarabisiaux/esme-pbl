def evaluate(board, ai_symbol, human_symbol):
  winner=board.winner()
  if winner == ai_symbol:
    return 10
  elif winner ==human_symbol:
    return -10
  return 0
  

def minimax(board, depth, maximizing, ai_symbol, human_symbol):
  score = evaluate(board, ai_symbol, human_symbol)

  if score != 0 or board.is_full() or depth==0:
    return score
  

