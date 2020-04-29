"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
maxDepth = 2


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
    xPlayed = 0
    oPlayed = 0
    for row in board:
        for column in row:
            if column == X:
                xPlayed = xPlayed + 1
            if column == O:
                oPlayed = oPlayed + 1

    if xPlayed > oPlayed:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleResults = []
    for i in range(3):
        for j in range(3):
            if (board[i][j]) == EMPTY:
                possibleResults.append((i, j))
    return possibleResults


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action == None):
        raise ValueError("Invalid action. Action Can't be None")

    if (board[action[0]][action[1]] != EMPTY):
        raise ValueError("Invalid action. The selected spot has already a selection")
    actionPlayer = player(board)
    returningBoard = copy.deepcopy(board)
    returningBoard[action[0]][action[1]] = actionPlayer
    return returningBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY):
        return board[0][0]
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY):
        return board[0][2]

    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY):
            return board[i][0]
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY):
            return board[0][i]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    if (winner(board) == O):
        return -1
    if (winner(board) == None):
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None

    nextPlayer = player(board)
    oponentPlayer = None
    bestAction = None
    bestActionUtility = None
    if(nextPlayer == X):
        bestActionUtility = -1
        oponentPlayer = O
    else:
        bestActionUtility = 1
        oponentPlayer = X

    for action in actions(board):
        if (bestAction == None):
            bestAction = action
        newBoard = result(board, action)
        actionUtility = minimaxRecursive(newBoard, 1, oponentPlayer)
        if(nextPlayer == X):
            if (actionUtility > bestActionUtility):
                bestAction = action
                bestActionUtility = actionUtility
        else:
            if (actionUtility < bestActionUtility):
                bestAction = action
                bestActionUtility = actionUtility


    return bestAction


def minimaxRecursive(board, depth, player):
    if (terminal(board) or depth == maxDepth):
        return utility(board)

    if player == X:
        bestVal = -1
        for action in actions(board):
            newBoard = result(board, action)
            value = minimaxRecursive(newBoard, depth+1, O)
            bestVal = max(bestVal, value)
        return bestVal

    else:
        bestVal = 1
        for action in actions(board):
            newBoard = result(board, action)
            value = minimaxRecursive(newBoard, depth+1, X)
            bestVal = min(bestVal, value)
        return bestVal
