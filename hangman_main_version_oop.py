

class Hangmangame():
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()
        self.number_of_attemps = 6

        self.HANGMAN_PICS = [
            """
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


    def display_hangman(self):
        missed_attemps = 6 - self.number_of_attemps
        print(self.HANGMAN_PICS[missed_attemps])

    def display_word(self):
        result = []
        for letter in self.word:
            if letter in self.guessed:
                result.append(letter)
            else:
                result.append(" _ ")
        return "".join(result)

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            print(f"Litera {letter} była juz zgadywana.")
            return False
        self.guessed.add(letter)
        if letter in self.word:
            print(f"Zgandales/as litere {letter}!")
            return True
        else:
            self.number_of_attemps -= 1
            print(f"Litera {letter} nie znajduje sie w słowie! Pozostało prób: {self.number_of_attemps}")
            return False

    def is_finished(self):
        if not " _ " in self.display_word():
            print(f"Wygrałes!")
            return True
        elif self.number_of_attemps == 0:
            print(f"Przegrałes!Słowo to: {self.word}")
            return True
        return False


game = Hangmangame("kurwa")

while not game.is_finished():
    print("Kategoria: you ")
    game.display_hangman()
    print(game.display_word())
    cos = input("Podaj litere: ")
    game.guess_letter(cos)


