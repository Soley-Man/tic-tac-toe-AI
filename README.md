# tic-tac-toe-AI
AI that learns to play tic tac toe through reinforcement learning. The algorithm creates a Memory dictionary in which different states of the board are stored and associated with the possible moves that the agent can take in that state. If the AI loses, the last move it took is removed from the possible moves associated with the board's last state. The AI thus unlearns the losing moves at every state of the game, thus only playing the winning moves (or at least the non-losing moves; ties are possible).

The first part of the algorithm involves two AIs playing against each other (sharing the same Memory to optimize their strategies and the training speed). Then the player may play against the AI (the player's symbol is 'X' and the AI's is 'O').
