class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def display(self):
        print()
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[+1]} | {self.cells[i+2]}")
            if i < 6:
                print("---+---+---")
        print()

    def update_cell(self, cell_no, player_symbol):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player_symbol
            return True
        return False







game = Board()
game.display()