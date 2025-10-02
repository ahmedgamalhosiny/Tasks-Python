import random


class Player:
    def __init__(self , name , symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self , board):
        pass


class HumanPlayer(Player):
    def make_move(self , board):
        while True:
            try:
                pos = int(input(f"{self.name} enter position (1-9): "))
                if pos < 1 or pos > 9:
                    print("position must be between 1 and 9")
                    continue
                if not board.update(pos , self.symbol):
                    print("that position is already taken")
                    continue
                break
            except Exception as e:
                print(f"error {e}")


class ComputerPlayer(Player):
    def make_move(self , board):
        while True:
            pos = random.randint(1 , 9)
            if board.update(pos , self.symbol):
                print(f"Computer chose position {pos}")
                break


class Board:
    def __init__(self):
        self.grid = [" " for _ in range(9)]

    def display(self):
        print("\n")
        print(f" {self.grid[0]} | {self.grid[1]} | {self.grid[2]} ")
        print("---+---+---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]} ")
        print("---+---+---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]} ")
        print("\n")

    def update(self , pos , symbol):
        if self.grid[pos-1] == " ":
            self.grid[pos-1] = symbol
            return True
        else:
            return False

    def check_winner(self):
        win_patterns = [
            (0 , 1 , 2) , (3 , 4 , 5) , (6 , 7 , 8) ,
            (0 , 3 , 6) , (1 , 4 , 7) , (2 , 5 , 8) ,
            (0 , 4 , 8) , (2 , 4 , 6)
        ]
        for a , b , c in win_patterns:
            if self.grid[a] == self.grid[b] == self.grid[c] != " ":
                return self.grid[a]
        return None

    def is_full(self):
        return " " not in self.grid

    def __str__(self):
        return f"{self.grid}"


class Game:
    def __init__(self , player1 , player2):
        self.board = Board()
        self.players = [player1 , player2]
        self.current_turn = 0

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"{current_player.name} wins with {winner}!")
                break
            if self.board.is_full():
                self.board.display()
                print("It is a draw!")
                break

            self.switch_turns()


def menu():
    print("\n=== Tic Tac Toe ===")
    print("1: Play with a friend")
    print("2: Play vs computer")

    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                name1 = input("Enter Player1 name: ")
                name2 = input("Enter Player2 name: ")
                p1 = HumanPlayer(name1 , "X")
                p2 = HumanPlayer(name2 , "O")
                g = Game(p1 , p2)
                g.play()
                break
            elif choice == 2:
                name1 = input("Enter your name: ")
                p1 = HumanPlayer(name1 , "X")
                p2 = ComputerPlayer("Computer" , "O")
                g = Game(p1 , p2)
                g.play()
                break
            else:
                print("please enter 1 or 2 only")
        except Exception as e:
            print(f"error {e}")


if __name__ == "__main__":
    menu()
