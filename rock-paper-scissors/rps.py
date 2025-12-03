#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

# These are the only three moves in the game
moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Player that always plays rock
class AllRockPlayer(Player):
    def move(self):
        return 'rock'


# This player picks a random move each time
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Human player gets input from the keyboard
class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, paper, or scissors? ").lower()
            if choice in moves:
                return choice
            else:
                print(
                    "That is not a valid move. Please type rock, paper, "
                    "or scissors."
                )


# This player copies whatever the opponent just did
class ReflectPlayer(Player):
    def __init__(self):
        self.last_opponent_move = None

    def move(self):
        if self.last_opponent_move is None:
            return random.choice(moves)
        return self.last_opponent_move

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move


# This player cycles through the moves: rock → paper → scissors → rock...
class CyclePlayer(Player):
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move is None:
            first = random.choice(moves)
            self.last_move = first
            return first

        if self.last_move == 'rock':
            next_move = 'paper'
        elif self.last_move == 'paper':
            next_move = 'scissors'
        else:
            next_move = 'rock'

        self.last_move = next_move
        return next_move

    # must remember its own last move
    def learn(self, my_move, their_move):
        self.last_move = my_move


# This checks if one move beats another using regular RPS rules
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Game class controls the entire match
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self, round_number):
        print(f"\nRound {round_number}")

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  |  Player 2: {move2}")

        if beats(move1, move2):
            print("Player 1 wins the round!")
            self.score1 += 1
        elif beats(move2, move1):
            print("Player 2 wins the round!")
            self.score2 += 1
        else:
            print("It's a tie!")

        print(f"Score -> Player 1: {self.score1} | Player 2: {self.score2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, rounds):
        print("Game start!")

        for r in range(1, rounds + 1):
            self.play_round(r)

        print("\nGame over!")
        print(
            f"Final Score -> Player 1: {self.score1} | Player 2: {self.score2}"
        )

        if self.score1 > self.score2:
            print("Player 1 wins the game!")
        elif self.score2 > self.score1:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")


# let user choose which players to use
if __name__ == '__main__':
    players = {
        '1': AllRockPlayer,
        '2': RandomPlayer,
        '3': ReflectPlayer,
        '4': CyclePlayer,
        '5': HumanPlayer
    }

    print("Player list:")
    for number, player in players.items():
        print(f"{number}. {player.__name__}")

    while (p1 := input("Choose player 1: ")) not in players.keys():
        print("Invalid choice, please select a valid player number.")

    while (p2 := input("Choose player 2: ")) not in players.keys():
        print("Invalid choice, please select a valid player number.")

    # Ask for number of rounds
    while True:
        try:
            rounds = int(input("How many rounds shall we play? "))
            if rounds > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    game = Game(players[p1](), players[p2]())
    game.play_game(rounds)
