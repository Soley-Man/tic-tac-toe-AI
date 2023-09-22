# tic-tac-toe-AI
AI that learns to play tic tac toe. The algorithm creates a Memory dictionary in which different states of the board are stored and associated with the possible moves that the agent can take in that state. If the AI loses, the last move it took is removed from the possible moves associated with the board's last state. The AI thus learns the winning moves at every state of the game.

The first part of the algorithm involves two AIs playing against each other (sharing the same Memory so to optimize their strategies and the algorithm speed). Then the player may play against the AI (the player's symbol is 'X' and the AI's is 'O').
