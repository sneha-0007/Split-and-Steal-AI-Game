# ai_engine.py

from minimax import minimax, MOVES

def get_best_move(opponent_last_move):
    """
    Main function to call from backend
    """

    best_move = None
    best_score = float('-inf')

    for move in MOVES:
        score = minimax(
            opponent_last_move,
            depth=2,              # small depth (important!)
            is_maximizing=False,
            alpha=float('-inf'),
            beta=float('inf')
        )

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
