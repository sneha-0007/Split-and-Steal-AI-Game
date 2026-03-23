# minimax.py

from utils import evaluate

MOVES = ["SPLIT", "STEAL"]

def minimax(opponent_last_move, depth, is_maximizing, alpha, beta):
    """
    Adapted Minimax for decision-based game
    """

    if depth == 0:
        return 0

    if is_maximizing:
        max_eval = float('-inf')

        for my_move in MOVES:
            for opp_move in MOVES:

                score = evaluate(my_move, opp_move)

                # bias towards opponent's last move
                if opp_move == opponent_last_move:
                    score += 2

                eval_score = score + minimax(
                    opponent_last_move,
                    depth - 1,
                    False,
                    alpha,
                    beta
                )

                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)

                # Alpha-Beta pruning
                if beta <= alpha:
                    break

        return max_eval

    else:
        min_eval = float('inf')

        for my_move in MOVES:
            for opp_move in MOVES:

                score = evaluate(my_move, opp_move)

                if opp_move == opponent_last_move:
                    score -= 2

                eval_score = score + minimax(
                    opponent_last_move,
                    depth - 1,
                    True,
                    alpha,
                    beta
                )

                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)

                if beta <= alpha:
                    break

        return min_eval
