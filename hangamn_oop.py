
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
        missed_attempts = 6 - self.number_of_attemps
        print(self.HANGMAN_PICS[missed_attempts])



    def display_word(self):
        result = []
        for letter in self.word:
            if letter in self.guessed:
                result.append(letter)
            else:
                result.append(" ___ ")
        return "".join(result)

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            print(f"The letter {letter} has already been guessed..")
            return False
        self.guessed.add(letter)
        if letter in self.word:
            print(f"You guessed the letter!")
            return True
        else:
            self.number_of_attemps -= 1
            print(f"The letter {letter} is not in the word. Attempts left: {self.number_of_attemps}")
            return False


    def is_finished(self):
        if not " ___ " in self.display_word():
            print(f"\nYou won!")
            return True
        elif self.number_of_attemps == 0:
            print(f"\nYou lost!Word is: {self.word}")
            return True
        return False


game = Hangmangame("maserati")  #word

while not game.is_finished():
    print()
    print(f"carbrand ")
    print()
    game.display_hangman()
    print(game.display_word())
    letter = input("\nEnter the letter: ")
    game.guess_letter(letter)