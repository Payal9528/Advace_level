from enum import Enum

class GameState(Enum):
    START = 1
    PLAY = 2
    PAUSE = 3
    GAME_OVER = 4

state = GameState.START

if state == GameState.START:
    print("Welcome to the game!")