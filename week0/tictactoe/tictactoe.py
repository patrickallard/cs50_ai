"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    global turn
    turn = 0

    if board.count(EMPTY) == 9:
        turn += 1
        return X
    elif (turn % 2) == 0:
        turn += 1
        return X
    else:
        turn += 1
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Only use spaces that are EMPTY
    row, col = board
    candidates = [
        ("upperleft", (row[0], col[0])),
        ("uppermiddle", (row[0], col[1])),
        ("upperright", (row[0], col[2])),
        ("middleleft", (row[1], col[0])),
        ("middle", (row[1], col[1])),
        ("middleright", (row[1], col[2])),
        ("bottomleft", (row[2], col[0])),
        ("bottommiddle", (row[2], col[1])),
        ("bottomright", (row[2], col[2])),
    ]

    actions = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                actions.add((candidates[0], (i, j)))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    copy = deepcopy(board)
    i,j = action

    if board[i][j] != None:
        raise Exception
    else:
        copy[i][j] = player_move

    return copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        # check vertical
            for row in board:
                if row == [player] * 3:
                    return player

        # check horizontal
            for i in range(3):
                column = [board[x][i] for x in range(3)]
                if column == [player] * 3:
                    return player

        # check diagonal
            if [board[i][i] for i in range(0, 3)] == [player] * 3:
                return player

            elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
                return player
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # game is won or no possible moves
    if ((winner(board) != None) or (board.count(EMPTY) == 0)):
        return True
    # moves still possible
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maxvalue(board):
        if terminal(board):
            return utility(board)
        else:
            v = float('-inf')
            for action in actions(board):
                v = maxvalue(v, minvalue(result(board, action)))
            return v

    def minvalue(board):
        if terminal(board):
            return utility(board)
        else:
            v = float('-inf')
            for action in actions(board):
                v = minvalue(v, maxvalue(result(board, action)))
            return v

    turn = player(board)

    if terminal(board):
        return None
    elif turn == X:
        return maxvalue()
    else:
        return minvalue()
