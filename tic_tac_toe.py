import random


def evaluate(board):
  if 'xxx' in board:
    return 'player x wins'
  elif 'ooo' in board:
    return 'player o wins'
  elif ' ' not in board:
    return 'Draw'
  else:
    return '-'

def move(board, mark, position): # Returns the game board with the given mark in the given position.
  board = list(board)
  board[position] = mark
  return ''.join(board)

def player_move(board):
  while True:
    position = int(input("Enter your move (0-19): "))
    if 0 <= position < 20 and board[position] == ' ':
      board = move(board, 'x', position)
      print(board) # print the board after each move
      return board
    print("Invalid move, try again.")

def pc_move(board): # Returns a game board with the computer's move.
  while True:
    position = random.randint(0, 19)
    if board[position] == ' ':
      board = move(board, 'o', position)
      print(board) # print the board after each move
      return board

def play_1D_tictactoe():
  board = ' ' * 20
  while True:
    board = player_move(board)
    result = evaluate(board)
    if result != '-':
      return result
    board = pc_move(board)
    result = evaluate(board)
    if result != '-':
      return result

print (play_1D_tictactoe())