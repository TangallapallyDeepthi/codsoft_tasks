# ==========================================================
# TASK 2 - TIC-TAC-TOE AI
# Artificial Intelligence Internship
# Minimax Algorithm
# ==========================================================

import math
import random


# ----------------------------------------------------------
# Display the board
# ----------------------------------------------------------

def print_board(board):
    print("\n")
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()


# ----------------------------------------------------------
# Check whether a player has won
# ----------------------------------------------------------

def check_winner(board, player):

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False


# ----------------------------------------------------------
# Check whether the board is full
# ----------------------------------------------------------

def is_board_full(board):
    return all(position in ["X", "O"] for position in board)


# ----------------------------------------------------------
# Minimax Algorithm
# ----------------------------------------------------------

def minimax(board, depth, is_maximizing):

    # AI wins
    if check_winner(board, "O"):
        return 10 - depth

    # Human wins
    if check_winner(board, "X"):
        return depth - 10

    # Draw
    if is_board_full(board):
        return 0

    # AI's turn - maximize score
    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] not in ["X", "O"]:

                board[i] = "O"

                score = minimax(board, depth + 1, False)

                board[i] = str(i + 1)

                best_score = max(best_score, score)

        return best_score

    # Human's turn - minimize score
    else:

        best_score = math.inf

        for i in range(9):

            if board[i] not in ["X", "O"]:

                board[i] = "X"

                score = minimax(board, depth + 1, True)

                board[i] = str(i + 1)

                best_score = min(best_score, score)

        return best_score


# ----------------------------------------------------------
# Find the best move for AI
# ----------------------------------------------------------

def find_best_move(board):

    best_score = -math.inf
    best_moves = []

    for i in range(9):

        if board[i] not in ["X", "O"]:

            board[i] = "O"

            score = minimax(board, 0, False)

            board[i] = str(i + 1)

            if score > best_score:
                best_score = score
                best_moves = [i]

            elif score == best_score:
                best_moves.append(i)

    # Randomly choose if multiple moves have same score
    return random.choice(best_moves)


# ----------------------------------------------------------
# Human Player Move
# ----------------------------------------------------------

def human_move(board):

    while True:

        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move] in ["X", "O"]:
                print("That position is already occupied.")
                continue

            board[move] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


# ----------------------------------------------------------
# Main Game
# ----------------------------------------------------------

def play_game():

    board = [str(i) for i in range(1, 10)]

    print("=" * 45)
    print("          🤖 TIC-TAC-TOE AI")
    print("=" * 45)

    print("\nYou are X")
    print("AI is O")

    print("\nBoard positions:")
    print_board(board)

    while True:

        # Human turn
        print("Your turn:")
        human_move(board)

        print_board(board)

        # Check human win
        if check_winner(board, "X"):
            print("🎉 Congratulations! You won!")
            break

        # Check draw
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

        # AI turn
        print("🤖 AI is thinking...")

        ai_move = find_best_move(board)
        board[ai_move] = "O"

        print(f"🤖 AI selected position {ai_move + 1}")

        print_board(board)

        # Check AI win
        if check_winner(board, "O"):
            print("🤖 AI wins! Better luck next time.")
            break

        # Check draw
        if is_board_full(board):
            print("🤝 It's a draw!")
            break


# ----------------------------------------------------------
# Start the game
# ----------------------------------------------------------

if __name__ == "__main__":
    play_game()