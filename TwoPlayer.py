from turtle import Turtle, Screen, onscreenclick

INITIAL_BOARD = [[None, None, None], [None, None, None], [None, None, None]]
COORDINATES = [
    [
        {"left": -240, "right": -81, "top": 240, "bottom": 81},
        {"left": -79, "right": 79, "top": 240, "bottom": 81},
        {"left": 81, "right": 240, "top": 240, "bottom": 81},
    ],[
        {"left": -240, "right": -81, "top": 79, "bottom": -79},
        {"left": -79, "right": 79, "top": 79, "bottom": -79},
        {"left": 81, "right": 240, "top": 79, "bottom": -79},
    ],[
        {"left": -240, "right": -81, "top": -81, "bottom": -240},
        {"left": -79, "right": 79, "top": -81, "bottom": -240},
        {"left": 81, "right": 240, "top": -81, "bottom": -240},
    ],
]


class TwoPlayer(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.draw_board()
        self.board = INITIAL_BOARD
        self.write_turtle = Turtle()
        self.player = "X"
        self.display_player()
        self.game_over = False
        self.play_game()
        self.screen.mainloop()


    def draw_board(self):
        self.teleport(x=-80, y=-240)
        self.setheading(90)
        self.forward(480)
        self.teleport(x=80, y=-240)
        self.forward(480)
        self.teleport(x=-240, y=-80)
        self.setheading(0)
        self.forward(480)
        self.teleport(x=-240, y=80)
        self.forward(480)
        self.hideturtle()


    def display_player(self):
        self.write_turtle.hideturtle()
        self.write_turtle.teleport(x=0, y=280)
        self.write_turtle.clear()
        self.write_turtle.write(f"Player {self.player}, it's your turn!", align="center", font=("Arial", 15, "normal"))


    def change_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"
        self.display_player()


    def find_square_clicked(self, x, y):
        print(x, y)
        for outer in range(3):
            for inner in range(3):
                if (COORDINATES[outer][inner]["left"] <= x <= COORDINATES[outer][inner]["right"]
                        and COORDINATES[outer][inner]["bottom"] <= y <= COORDINATES[outer][inner]["top"]):

                    self.check_square(outer, inner)
                    break
        self.check_for_win()
        if self.game_over:
            self.clear()
            self.write_turtle.clear()
            TwoPlayer()
        else:
            self.play_game()


    def check_square(self, outer: int, inner: int):
        print(outer, inner)
        if self.board[outer][inner] is None:
            if self.player == "X":
                self.pencolor("blue")
                self.teleport(COORDINATES[outer][inner]["left"], COORDINATES[outer][inner]["bottom"])
                self.setheading(45)
                self.forward(226.3)
                self.teleport(COORDINATES[outer][inner]["right"], COORDINATES[outer][inner]["bottom"])
                self.setheading(135)
                self.forward(226.3)
            else:
                self.pencolor("red")
                self.teleport(COORDINATES[outer][inner]["right"] - 20, COORDINATES[outer][inner]["top"] - 20)
                self.circle(80)
        self.board[outer][inner] = self.player
        print(self.board)
        self.change_player()

    def check_for_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and not row[0] is None:
                winner = row[0]
                print(winner)
                self.game_over = True
                return
        for inner in range(3):
            if self.board[0][inner] == self.board[1][inner] == self.board[2][inner] and not self.board[0][inner] is None:
                winner = self.board[0][inner]
                print(winner)
                self.game_over = True
                return
        centre = self.board[1][1]
        if ((self.board[0][0] == self.board[2][2] == centre and not centre is None)
            or (self.board[0][2] == self.board[2][0] == centre and not centre is None)):
            winner = centre
            print(winner)
            self.game_over = True
            return





    def play_game(self):
        onscreenclick(self.find_square_clicked)