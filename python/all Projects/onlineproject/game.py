# names = ['Rupok', 'Rishan', 'Gaza']

# # # [5, 6, 4]
# # name_len=[0]
# # for name_len  in names:
# #     name_len+=1
# #     print(name_len)
# names_len = []
# for display in names:
#     i = 0
#     for z in display:
#         i += 1
#     names_len.append(i)

# print(names_len)
# import random
# continues = True
# computer = random.randint(1, 10)
# while continues:
#     user = int(input("Enter A Number Between 1 to 10 :"))
#     if user == computer:
#         continues == False
#         print("congratulation You win .")
#         print(f"Computer was chosen {computer}")
#         break

#     if user > computer:
#         print("Guess Lower number")
#     elif user < computer:
#         print("Guess Higher number")
# import random

# a = int(input("Enter A guessed Number:"))


# def computer(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c' and low != high:
#         guess = random.randint(low, high)
#         feedback = input(
#             f"is {guess} too high (h) too low (l) or correct (c)   ? :")
#         if feedback == 'h':
#             high = guess-1
#         elif feedback == 'l':
#             low = guess+1

#     print(f"yay {x} was your  guessed  number  computer win..")


# computer(a)
# import math
# import random


# class player:
#     def __init__(self, letter):
#         self.letter = letter

#     def get_move(self, game):
#         pass


# class randomcom(player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self, game):
#         sqare = random.choice(game.available())
#         return sqare


# class human(player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self, game):
#         valid_sqare = False
#         val = None
#         while not valid_sqare:
#             sqare = input(self.letter + '\' s turn.Input move(0-9):')
#             try:
#                 val = int(sqare)
#                 if val not in game.available():
#                     raise ValueError
#             except ValueError:
#                 print("invalid sqare .try again.")
#         return val


# class tctac:
#     def __init__(self):

#         self.board = [' ' for _ in range(9)]
#         self.current = None

#     def print_board(self):
#         for row in [self.board[i*3:(i*1)*3]for i in range(3)]:
#             print('|'+'|'.join(row)+'|')

#     @staticmethod
#     def print_board_nums():
#         number_board = [[str(i)for i in range(j*3, (j+1)*3)]for j in range(3)]
#         for row in number_board:
#             print('|'+'|'.join(row)+'|')

#     def available(self):
#         moves = []
#         for (i, spot) in enumerate(self.board):
#             if spot == ' ':
#                 moves.append(i)
#         return moves

#     def empty_sqares(self):
#         return ' ' in self.board

#     def num_empty_sqares(self):
#         return self.board.count(' ')

#     def make_move(self, sqare, letter):
#         if self.board[sqare] == ' ':
#             self.board[sqare] = letter
#             return True
#         return False


# def play(game, x_player, o_player, print_game=True):

#    if print_game:
#         game.print_board_nums()
#     letter = 'x'

#    while game.empty_sqares():
#        if letter=='o':
#            sqare=o_player.get_move(game)
#        else:
#            sqare=x_player.get_move(game)
#        if game.make_move(sqare,letter):
#            if print_game:
#                print(letter+f'makes a move to sqare {sqare}')
#                game.print_board()
#                print('')
#            letter='O' if letter=='X'else'X'
# import random


# class Player:
#     def __init__(self, letter):
#         self.letter = letter

#     def get_move(self, game):
#         pass


# class RandomCom(Player):
#     def get_move(self, game):
#         square = random.choice(game.available())
#         return square


# class Human(Player):
#     def get_move(self, game):
#         valid_square = False
#         val = None
#         while not valid_square:
#             square = input(f'{self.letter}\'s turn. Input move (0-8): ')
#             try:
#                 val = int(square)
#                 if val not in game.available():
#                     raise ValueError(
#                         f"Square {val} is not available. Choose another.")
#                 valid_square = True
#             except ValueError as e:
#                 print(e)
#         return val


# class TicTacToe:
#     def __init__(self):
#         self.board = [' ' for _ in range(9)]

#     def print_board(self):
#         for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
#             print('|' + '|'.join(row) + '|')

#     @staticmethod
#     def print_board_nums():
#         number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)]
#                         for j in range(3)]
#         for row in number_board:
#             print('|' + '|'.join(row) + '|')

#     def available(self):
#         return [i for i, spot in enumerate(self.board) if spot == ' ']

#     def empty_squares(self):
#         return ' ' in self.board

#     def num_empty_squares(self):
#         return self.board.count(' ')

#     def make_move(self, square, letter):
#         if self.board[square] == ' ':
#             self.board[square] = letter
#             if self.winner(square, letter):
#                 return True
#         return False

#     def winner(self, square, letter):
#         # Check the row
#         row_ind = square // 3
#         row = self.board[row_ind * 3:(row_ind + 1) * 3]
#         if all([spot == letter for spot in row]):
#             return True

#         # Check the column
#         col_ind = square % 3
#         column = [self.board[col_ind + i * 3] for i in range(3)]
#         if all([spot == letter for spot in column]):
#             return True

#         # Check diagonals
#         if square % 2 == 0:
#             diagonal1 = [self.board[i]
#                          for i in [0, 4, 8]]  # left to right diagonal
#             if all([spot == letter for spot in diagonal1]):
#                 return True
#             diagonal2 = [self.board[i]
#                          for i in [2, 4, 6]]  # right to left diagonal
#             if all([spot == letter for spot in diagonal2]):
#                 return True

#         # If all checks fail
#         return False


# def play(game, x_player, o_player, print_game=True):
#     if print_game:
#         game.print_board_nums()

#     letter = 'X'  # Starting letter

#     while game.empty_squares():
#         if letter == 'O':
#             square = o_player.get_move(game)
#         else:
#             square = x_player.get_move(game)

#         if game.make_move(square, letter):
#             if print_game:
#                 print(f'{letter} makes a move to square {square}')
#                 game.print_board()
#                 print('')

#             if game.winner(square, letter):
#                 if print_game:
#                     print(f'{letter} wins!')
#                 return letter  # Return the winner's letter

#             # Alternate letters
#             letter = 'O' if letter == 'X' else 'X'

#     if print_game:
#         print('It\'s a tie!')
#     return None  # Return None for a tie


# if __name__ == '__main__':
#     x_player = Human('X')
#     o_player = RandomCom('O')
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game=True)
