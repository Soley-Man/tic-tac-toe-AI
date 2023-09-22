import random

Board = ['_' for _ in range(9)]
Memory = dict()



# FUNCTIONS #
def check_win(symbol: str) -> bool:
    """ Check if the agent's symbol is in any straight line of three in the board, therefore winning the game.
    Note: symbol should only be 'X' or 'O', or whichever two other symbols the agents use to play.
    
    >>> check_win('X') #where Board = ['X', 'X', 'X', 'O', 'X', '_', 'O', 'O', '_']
    True 
    >>> check_win('O') #where Board is the same as above
    False
    """
    
    # Horizontal 3 in a row
    if Board[0] == symbol and Board[1] == symbol and Board[2] == symbol: return True
    elif Board[3] == symbol and Board[4] == symbol and Board[5] == symbol: return True
    elif Board[6] == symbol and Board[7] == symbol and Board[8] == symbol: return True
    
    # Vertical 3 in a row
    elif Board[0] == symbol and Board[3] == symbol and Board[6] == symbol: return True
    elif Board[1] == symbol and Board[4] == symbol and Board[7] == symbol: return True
    elif Board[2] == symbol and Board[5] == symbol and Board[8] == symbol: return True
    
    # Diagonal 3 in a row
    elif Board[0] == symbol and Board[4] == symbol and Board[8] == symbol: return True
    elif Board[2] == symbol and Board[4] == symbol and Board[6] == symbol: return True
    
    else: return False

def possible_moves(board_state: list) -> list:
    """ Return a list of possible positions on the board where making a move is possible,
    e.g. the indexes of the open spaces.
    
    >>> possible_moves() #where Board = ['X','O','O', '_', '_', '_', 'X', 'X', 'O']
    [4, 5, 6]
    """
    return [idx for idx, value in enumerate(board_state) if value == '_']


def print_board():    
    """Print the board in a legible way.
    >>> print_board()
    ['_' '_' '_']
    ['X' '_' '_']
    ['O' '_' '_']
    """
    
    print(Board[:3])
    print(Board[3:6])
    print(Board[6:9])
    

    
class AI():
    def __init__(self, symbol):
        self.symbol = symbol
        self.action_taken = None
        self.previous_board_state = None
        
    def board_to_memory(self, board_state: list) -> list:
        """ Convert the state of the Board (relative to the agent's symbol) to a key to be stored in the memory.
        Note: symbol should either be 'X' or 'O', or whichever symbols the agents are using when playing.
        
        >>> AI.board_to_memory('X') #where Board = ['X','O','O', '_', '_', '_', 'X', 'X', 'O'] and agent's symbol is "X"
        '122000112'
        >>> AI.board_to_memory('O') #where Board is as above and agent's symbol is "O"
        '211000221'
        """
        
        converted_state = ''
        
        for value in board_state:
            if value == '_': converted_state += '0'
            elif value == self.symbol: converted_state += '1'
            elif value != self.symbol: converted_state += '2'
            
            
        return converted_state
        
    def resolve_loss(self):
        """ Resolves a loss by storing in the Memory the previous board state and removing 
        the last action taken from the available actions to take when that board state is re-encountered.
        i.e. The agent remembers the action that made it lose in that board state.
        """
        
        if self.board_to_memory(self.previous_board_state) in Memory:
            Memory[self.board_to_memory(self.previous_board_state)].remove(self.action_taken)
        else:
            Memory[self.board_to_memory(self.previous_board_state)] = possible_moves(self.previous_board_state)
            Memory[self.board_to_memory(self.previous_board_state)].remove(self.action_taken)        
        
    def take_turn(self):
        """
        Algorithm to take a turn:
        -Check if lost (if opponent won):
           if loss: resolve_loss(previous_board_state, action_taken)
              if previous_board_state is in memory, remove action_taken from available actions in that state.
              elif previous_board_state is not in memory, add it and remove action_taken from available actions in that state.
              end the game.
        -If not lost, check if the game is a tie (if there are no more possible actions to take AND no one has won)
        -See available actions:
        Check if memory of current board state exists:
           if not, choose random action from possible_actions().
           if yes:
              if there are no actions available to take, resolve a loss. (this is like the AI forfeiting the game because it can't win)
              else, choose random action from available actions in the memory.
        -Remember action taken: Store action to be taken in a variable action_taken.*
        -Remember board state: Store board state in a variable previous_board_state.*
        -Take the action, thus modifying the board state.
        
        *These variables will be useful in case the opponent wins: the agent will learn not to choose the action_taken when faced with the previous_board_state.
        
        """
        
        if self.symbol == 'X': opponent_symbol = 'O'
        elif self.symbol == 'O': opponent_symbol = 'X'
        
        #Check if the agent lost the game:
        if check_win(opponent_symbol):
            self.resolve_loss()
            return 'END'
        
        #Check if the game is tied
        elif len(possible_moves(Board)) == 0:
            return 'END'
        
        #Else, take the turn
        else:
            # See available actions, resolve loss if no potentially winning moves available
            if self.board_to_memory(Board) in Memory:
                available_actions = Memory[self.board_to_memory(Board)]
                
                # If no actions that can help win, forfeit and resolve loss
                if len(available_actions) == 0:
                    self.resolve_loss()
                    return 'END'
                    
            else:
                available_actions = possible_moves(Board)
                
            # Take an action
            self.action_taken = random.choice(available_actions)
            self.previous_board_state = Board.copy()
            Board[self.action_taken] = self.symbol
            
            





# Training AI vs AI
AI1 = AI('X')
AI2 = AI('O')

for _ in range(100000):
    Board = ['_' for _ in range(9)] #reset the Board
    while True:
        if AI1.take_turn() == 'END':
            break
        if AI2.take_turn() == 'END':
            break
        


# Player vs AI Game:
print('\nBoard Position Indexes:')
print(['0', '1', '2'])
print(['3', '4', '5'])
print(['6', '7', '8'])
print()

AI_opponent = AI('O')
player_symbol = 'X'

Board = ['_' for _ in range(9)] #reset the Board

while True:
    print_board()
    
    # Check end of game conditions
    if check_win(AI_opponent.symbol):
        print('AI WINS!')
        break
    elif check_win(player_symbol):
        print('PLAYER WINS!')
    elif len(possible_moves(Board)) == 0:
        print('TIE!')
        break
    
    # Player turn
    while True:
        player_move = int(input('Input move index: '))
        if player_move in possible_moves(Board):
            break
        else: print('Invalid move - try again')
        
    Board[player_move] = player_symbol
    
    #AI turn
    AI_opponent.take_turn()
    