class TicTacToe:
    WINNING_COMBINATIONS = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    def __init__(self):
        self.board = [[" "]*3 for i in range(3)]

    def __repr__(self):
        return ("\n"+"-"*9+"\n").join([" | ".join(row) for row in self.board])

    def get(self, position):
        return self.board[(position-1)/3][(position-1)%3]

    def set(self, player, position):
        self.board[(position-1)/3][(position-1)%3] = player.upper()

    def isEmpty(self, position):
        return self.get(position) == " "

    def makeMove(self, player, position):
        if self.isEmpty(position) is True:
            self.set(player, position)
        else:
            raise Exception("Invalid position")

    def won(self, player, last_pos):
        possible_combinations = []
        for combination in self.WINNING_COMBINATIONS:
            if last_pos in combination:
                possible_combinations.append(combination)

        for combination in possible_combinations:
            won = 0
            for i in combination:
                if self.get(i) == player:
                    won += 1

            if won == 3:
                return True

        return False

    def validMoves(self):
        validMoves = []
        for i in range(1, 10):
            if self.isEmpty(i):
                validMoves.append(str(i))

        return validMoves

    def printValidMoves(self):
        print ",".join(self.validMoves())

class Cli:
    def __init__(self, starting_player):
        self.board = TicTacToe()
        self.curr_player = starting_player

    def play(self):
        print "-"*80
        print "Player " + self.curr_player
        print "-"*80
        print self.board
        self.last_position = self.makeValidMove()
        if self.board.won(self.curr_player, self.last_position) is True:
            print "Player " + self.curr_player + " won!\nCongratulations!!"
        else:
            self.curr_player = "X" if self.curr_player == "O" else "O"
            self.play()




    def makeValidMove(self):
        position = input("Enter the position where you want to have your flag: ")
        try:
            self.board.makeMove(self.curr_player, position)
        except Exception, e:
            print str(e)
            print "Valid moves: "
            self.board.printValidMoves()
            return self.makeValidMove()
        return position


game=Cli("X")
game.play()
