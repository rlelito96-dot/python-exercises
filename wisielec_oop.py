
class HangmanGame():
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()
        self.number_of_attemps = 6
        self.hangman_pics = [
        r"""
         +---+
         |   |
             |
             |
             |
             |
        =========""",
        r"""
         +---+
         |   |
         O   |
             |
             |
             |
        =========""",
        r"""
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========""",
        r"""
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========""",
        r"""
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========""",
        r"""
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========""",
        r"""
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        ========="""
        ]

    def hangman_display(self):
        missed_attemps = 7 - self.number_of_attemps
        print(self.hangman_pics[missed_attemps])


    def display_word(self):
        result = []
        for letter in self.word():
            if letter in self.guessed:
                result.append(letter)
            else:
                result.append(" _ ")
        return result

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            print(f"Litera {letter} była juz zgadywana.")
            return False
        self.guessed.add(letter)

        if letter in self.word():
            print(f"Zgadnales/as {letter}!")
            return True
        else:
            self.number_of_attemps -= 1
            print(f"Litera {letter} nie znajduje sie w słowie.Pozostało prób: {self.number_of_attemps}")
            return False

    def is_finished(self):
        if " _ " not in display_word():
            print(f"Wygrałeś!")
            return True
        elif self.number_of_attemps == 0:
            print(f"Przegrałeś!Słowo to: {self.word}")
            return True
        return False

game = HangmanGame("Hiba")

while not game.is_finished():
    print("\nCategory: ")
    print()
    print(game.hangman_display())
    print(game.display_word())
    user = input("\nPodaj litere: ")
    game.guess_letter(user)


