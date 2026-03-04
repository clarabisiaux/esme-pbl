def evaluate(board, ai_symbol, human_symbol): #score to know who the winner is
  winner=board.winner()
  if winner == ai_symbol:
    return 10
  elif winner == human_symbol:
    return -10
  return 0
  

def minimax(board, depth, maximizing, ai_symbol, human_symbol):
    score = evaluate(board, ai_symbol, human_symbol)

    if score != 0 or board.is_full() or depth == 0:
        return score, []

    if maximizing:
        best = -1000
        best_path = []

        for move in board.available_moves():
            board.grid[move] = ai_symbol
            val, path = minimax(board, depth-1, False, ai_symbol, human_symbol)
            board.grid[move] = " "

            if val > best:
                best = val
                best_path = [move] + path

        return best, best_path

    else:
        best = 1000
        best_path = []

        for move in board.available_moves():
            board.grid[move] = human_symbol
            val, path = minimax(board, depth-1, True, ai_symbol, human_symbol)
            board.grid[move] = " "

            if val < best:
                best = val
                best_path = [move] + path

        return best, best_path

def best_move(board, depth, ai_symbol, human_symbol):
    best_score = -1000
    move_choice = None
    scores = []  # ← liste pour stocker les scores
    score, path = minimax(board, depth-1, False, ai_symbol, human_symbol)
    print("Ideal AI winning sequence:", [move] + path)

    for move in board.available_moves():
        board.grid[move] = ai_symbol
        score = minimax(board, depth-1, False, ai_symbol, human_symbol)
        board.grid[move] = " "

        scores.append((move, score))  # ← on stocke chaque score

        if score > best_score:
            best_score = score
            move_choice = move
    print("\nIdeal opponent winning sequence:")

    worst_score = 1000
    worst_path = []

    for move in board.available_moves():
        board.grid[move] = human_symbol
        val, path = minimax(board, depth-1, True, ai_symbol, human_symbol)
        board.grid[move] = " "

        if val < worst_score:
            worst_score = val
            worst_path = [move] + path

    print(worst_path)

    # ---- PRINTS DEMANDÉS ----
    print("\nGeneration scores:")
    for move, score in scores:
        print(f"Move {move} → Score {score}")

    print("Minimum score:", min(score for _, score in scores))
    print("Maximum score:", max(score for _, score in scores))

    return move_choice
  
  for move in board.available_moves(): #try all the possible moves
    board.grid[move] = ai_symbol
    score = minimax(board, depth-1, False, ai_symbol, human_symbol) #score for each move
    board.grid[move] = " "
    if score>best_score: #keep the best score
      best_score = score
      move_choice = move
      
    return move_choice



