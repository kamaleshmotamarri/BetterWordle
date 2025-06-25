# BetterWordle

Better Wordle is a terminal-based word guessing game inspired by the original Wordle, but with more flexibility. This version allows players to choose the length of the word they want to guess, ranging from three to seven letters. The game then selects a random English word of that length and gives the player a limited number of attempts to guess it correctly.

After each guess, the game provides feedback indicating which letters are correct and in the correct position, which letters are correct but in the wrong position, and which letters are not in the word at all. This feedback helps guide the player toward the correct answer. The game uses a word list from the Natural Language Toolkit (NLTK) to select valid English words.

To play the game, the player first selects a word length between three and seven letters. The game then generates a random word of that length and allows the player to begin guessing. The number of guesses allowed is equal to the word length plus one. If the player guesses the word correctly within the allowed number of attempts, they win. Otherwise, the correct word is revealed after the final guess.

The game requires Python and the nltk library. Before running the game, users should ensure that nltk is installed and the English word corpus is downloaded. Once ready, the game can be run from the terminal or command prompt, and it will guide the user through each step. After each game, the player is given the option to play again.
