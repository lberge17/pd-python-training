import os
import sys

cwd = os.getcwd()
sys.path.append(cwd + "/lib")

from cli import Cli
from game import Game
from board import Board
from player import Player
from players.computer import Computer
from players.human import Human