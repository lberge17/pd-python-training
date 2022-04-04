# Tic Tac Toe W/ AI (Python Edition)
This README and all parts of this project build are borrowed from the original learn-co-curriculum's tic tac toe w/ai in ruby and translated to python for this project.

## Objectives
* Build a command-line interface (CLI).
* Create a domain model with multiple relating and collaborating objects.

## Overview
The goal of this project is to build a version of Tic-tac-toe with 0-, 1-, and 2-player modes:

* A 0-player game has two computer players playing against each other with no interaction from the user.
* A 1-player game has a human playing against a computer.
* A 2-player game has two human players.
You'll be implementing Tic-tac-toe using multiple objects that relate and collaborate, including separate classes for human players and computer players. The computer player class will have some sort of artificial intelligence or logic to make move decisions. Finally, you'll wrap all of this up in a CLI.

## Requirements
* 0, 1, or 2 player Tic-tac-toe.
* Command Line Interface
* Computer AI
```
Project Structure
├── README.md
├── bin
│   └── tictactoe
├── config
│   └── environment.py
├── lib
    ├── players
        ├── computer.py
        └── human.py
    ├── board.py
    ├── game.py
    └── player.py
```

lib - Tic-tac-toe models
You will be implementing Tic-tac-toe through a domain model that uses multiple classes to encapsulate the different logical components and units in Tic-tac-toe.

board.py - Board
The Board class represents the data and logic of a Tic-tac-toe game board. It has a property, cells, that stores the data of the state of the board in an list. The #reset! function can reset the state of the cells to what a board should look like at the start of a game, an list with 9 " " elements.

When a board is initialized, it should start with cells for a new game of Tic-tac-toe. You can and should use #reset!.

A board can print its current state with the #display function.

You'll also build a #position function that takes in the user's input in the form of 1-9 strings like "2" or "9" and looks up the value of the cells at the correct index from the list's perspective. All other functions will take input in the user's perspective of 1-9 strings and use #position to look up the value according to the cells' list index.

Similarly, you're going to build an #update function that represents updating the board when a player makes a move. This function will take two arguments, the first will be the position the user wants to occupy in the form of 1-9 strings that you will need to convert to the board cells' list index, along with the player object making the move. When you update the appropriate index in the cells, you will set it equal to the token of the player object by calling the #token method on the player.

Finally, a board can return values based on its state such as #full? when entirely occupied with "X" and "O"s and a #turn_count based on how many positions in the cells list are filled. #taken? will return true or false for an individual position. #valid_move? will ensure that moves are between 1-9 and not taken.

player.py - Player
The Player class is not actually a valid player of Tic-tac-toe but rather a root class that will act as an inheritance point for actual player classes such as Human(Player) and Computer(Player). The Player root class will define only the most basic properties of a player, that they have a token property that can be set upon initialization.

Every player subclass will implement a #move method that represents how that type of player makes a move in Tic-tac-toe.

'players/human.py' - Human
Define a class Human that inherits from Player. 

The human player must implement a #move method that takes in a board argument and allows a human player to enter a move via the CLI. The method should return the value the user enters. Even though the method accepts a board argument, it does not need to use it.

game.py - Game
The Game class is the main model of the application and represents a singular instance of a Tic-tac-toe session.

A game has one Board through its board property.
A game has two Players stored in a player_1 and player_2 property.
Board and Player do not directly relate to the Game but do collaborate with each other through arguments.

Beyond providing relationships with players and a board, the Game instance must also provide the basic game runtime and logic. These methods relate to the state of the game such as #current_player, #won?, and #winner. The other methods relate to managing a game, like #start, #play, and #turn.

'players/computer.py'
Define a class Computer that represents a computer player of Tic-tac-toe. Implement a #move method that accepts a board and returns the move the computer wants to make in the form of a 1-9 string. How the computer decides to make that move is up to you but it must be capable of returning a valid move at some point.

def move(board):
  "1"

Returns a valid move for the first move but after that your program will go into an infinite loop because the computer will constantly try to occupy the "1" position in the board even though it is already occupied. So don't do that.

Think about the levels of intelligence you can build into this method. Start with the simplest level of intelligence, and get more and more complicated. Each step of the way you should have a working computer player though.

Remember, Tic-tac-toe when played perfectly is unwinnable. You should strive to build computer logic that when the computer plays, the game is unwinnable. You can hardcode your logic, things like "On turn 1 always try to go in the middle if you can" and if not "try to go in a corner" or any logic tree you can think of - there is an algorithm called Min/Max, but it's going to be hard to implement given our current implementation of a Game, so we recommend building something that's a more colloquial or condition-based algorithm.

bin/tictactoe
The requirements of your CLI are as follows, free for you to implement however you see fit.

Greet the user with a message.
Prompt the user for what kind of game they want to play, 0,1, or 2 player.
Ask the user for who should go first and be "X".
Use the input to correctly initialize a Game with the appropriate player types and token values.
When the game is over, the CLI should prompt the user if they would like to play again and allow them to choose a new configuration for the game as described above. If the user doesn't want to play again, exit the program.
You can implement this logic within the bin/tictactoe directly or encapsulate it within Game via a method like #start and simply evoke that method in the CLI. There is no wrong way to implement code that works.

If you'd like, implement a "wargames" game type. When asked what kind of game they want to play or for the number of players, if the user types in "wargames", have the computer play itself 100 times and report how many times the game was won. This is not a requirement, it would just be fun. A perfect computer AI should never be able to win, like in the case of thermonuclear war.

The rest is up to you and your team. Have fun, implement the spirit of the project, meet the requirements as you interpret them, be creative, and don't worry, there are no wrong answers with code.