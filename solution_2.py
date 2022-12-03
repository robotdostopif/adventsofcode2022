from base import Solution
from enum import Enum

class PlayerMoves(str, Enum):
    A = "ROCK"
    
    B = "PAPER"
    
    C = "SCISSOR"
    
    X = "ROCK"
    
    Y = "PAPER"
    
    Z = "SCISSOR"
    
    
class Score(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    
    
class Winner(str, Enum):
    ROCK = "SCISSOR"
    PAPER = "ROCK"
    SCISSOR = "PAPER"
    
    
class Looser(str, Enum):
    ROCK ="PAPER"
    PAPER = "SCISSOR"
    SCISSOR = "ROCK"
    
    
class Outcome(str, Enum):
    X = "LOSE"
    Y = "DRAW"
    Z = "WIN"
    
    
class Game:
    def __init__(self, moves):
        self.moves = moves
        self.player_score = 0
        self.opponent_score = 0
    def play(self, part=1):
        for move in self.moves:
            opponent, player = move.split(" ")
            
            if part == 2:
                opponent_move = PlayerMoves[opponent].value
                if Outcome[player].value == "LOSE":
                    player_move = Winner[opponent_move].value
                elif Outcome[player].value == "WIN":
                    player_move = Looser[opponent_move].value
                else:
                    player_move = opponent_move
            
            
            if Winner[player_move].value == opponent_move: 
                self.player_score += 6
            elif Winner[opponent_move].value == player_move:
                self.opponent_score += 6
            else:
                self.player_score += 3
                self.opponent_score += 3
            
            """ Score for each round """
            self.player_score += Score[player_move].value
            self.opponent_score += Score[opponent_move].value
                
            print(f"Opponent Score: ", self.opponent_score)
            print(f"Player Score: ", self.player_score)
            self.player_score = 0
            self.opponent_score = 0



class Solution_2_1(Solution):
    def __init__(self, day, part):
        super(Solution_2_1, self).__init__(day, part)
    
    def solution(self):
        moves = self.import_text()
        game = Game(moves)
        game.play()
        game.play(part=2)
    
solution_2_1 = Solution_2_1(2, 1)
solution_2_1 = solution_2_1.solution()