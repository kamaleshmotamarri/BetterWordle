# Better Wordle
import random
import nltk 
nltk.download('words')
from nltk.corpus import words 

class BetterWordle:

    def __init__(self, word_length):
        self.word_length = word_length
        self.word_list = []
        self.guesses_allowed = self.word_length + 1
        self.number_of_guesses = 0
        self.correct_word_list = ["🟢" for _ in range(self.word_length)]

    def __repr__(self):
        return f"Wordle({self.word_length})"

    def generate_word(self, length):
        english_words = [word.lower() for word in words.words() if len(word) == length and word.isalpha()]
        return random.choice(english_words) if english_words else None

    def create_wordlelist(self, selected_word, generated_word):
        self.user_word = []
        used_letters = [False] * len(generated_word)

        
        for i in range(len(selected_word)):
            if selected_word[i] == generated_word[i]:
                self.user_word.append("🟢")
                used_letters[i] = True
            else:
                self.user_word.append(None)

        
        for i in range(len(selected_word)):
            if self.user_word[i] is None:  
                if selected_word[i] in generated_word:
                    for j in range(len(generated_word)):
                        if selected_word[i] == generated_word[j] and not used_letters[j]:
                            self.user_word[i] = "🟡"
                            used_letters[j] = True
                            break
                if self.user_word[i] is None:
                    self.user_word[i] = "🔴"

        return self.user_word

    def main_game(self):
        self.the_word = self.generate_word(self.word_length) 
        if not self.the_word:
            print("No valid words found for the selected length. Exiting game.")
            return

        print(f"A {self.word_length}-letter word has been generated. Start guessing!")
        while self.number_of_guesses < self.guesses_allowed:
            self.user_word_guess = input(f"Guess a word of length {self.word_length}: ").lower().strip()

            
            while len(self.user_word_guess) != self.word_length or not self.user_word_guess.isalpha():
                self.user_word_guess = input(f"Please enter a valid word of length {self.word_length}: ").lower().strip()

            if self.user_word_guess == self.the_word:
                print(self.correct_word_list)
                print(f"Congratulations! You've guessed the word: {self.the_word}")
                return

         
            self.number_of_guesses += 1
            feedback = self.create_wordlelist(self.user_word_guess, self.the_word)
            print("Feedback:", "".join(feedback))
            print(f"Guesses remaining: {self.guesses_allowed - self.number_of_guesses}")

       
        print(f"Sorry, you've run out of guesses. The word was: {self.the_word}")

if __name__ == "__main__":
    play_again = True
    while play_again:
        print("Welcome to Better Wordle!")
        user_length_choice = int(input("How many letters do you want in your word? (3-7) "))
        while user_length_choice < 3 or user_length_choice > 7:
            user_length_choice = int(input("Please enter a number between 3 and 7: "))

        game = BetterWordle(user_length_choice)
        game.main_game()

        play_again_input = input("Do you want to play again? yes or no: ").lower().strip()
        while play_again_input not in ["yes", "no"]:
            play_again_input = input("Please enter 'yes' or 'no': ").lower().strip()
        play_again = play_again_input == "yes"
    print("Thanks for playing Better Wordle, This was build by Kamalesh!")

