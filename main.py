import re

class WordleValidationError(Exception):
    pass
    # def __init__(self, message):
    #    self.message = message
    #    super.__init__()


class WordleSolver:

    absent_letters = []
    possible_words = {}

    def __init__(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                word, freq = line.split(',')
                word = word.lower()
                self.possible_words[word] = int(freq.strip())

    def check_letter_against_symbol(self, guessed_letter, word_letter, match_symbol, word):
        
        if match_symbol == 'g':
            if word_letter != guessed_letter:
                del self.possible_words[word]
                return True    

        elif match_symbol == 'y':
            if word_letter == guessed_letter or guessed_letter not in word:
                del self.possible_words[word]
                return True
        return False

    def can_filter_word(self, word, guess, matching_pattern):
        
        for index, letter in enumerate(word):
            symbol = matching_pattern[index]
            guessed_letter = guess[index]

            if self.check_letter_against_symbol(guessed_letter, letter, symbol, word):
                return True 
        return False

    def filter_words(self, guess, matching_pattern):
            
        for index, symbol in enumerate(matching_pattern):
            if symbol == '_':
                self.add_to_absent_letters(guess[index])

        original_list = self.possible_words.copy()
        
        for pw in original_list:
            # Remove word from potential words based on eliminated letters
            if self.contains_absent_letters(pw):
                del self.possible_words[pw]
                continue

            # Attempt to remove word based on G and Y rules
            if self.can_filter_word(pw, guess, matching_pattern):
                continue

    def add_to_absent_letters(self, letter_list):
     
        for letter in letter_list:
            self.absent_letters.append(letter)

    def contains_absent_letters(self, word):
        for letter in self.absent_letters:
            if letter in word:
                return True 
        return False 
    
    def validate_input(self, pattern, word):
        if re.match(pattern, word) is None:
            raise WordleValidationError("Input is not valid")

def main():
    ws = WordleSolver('freq.csv')
    while len(ws.possible_words) > 1:

        valid_input = False 
        while not valid_input:
            try:
                word_guess = input('Enter guessed word: ').lower()
                ws.validate_input('^[a-z]{5}$', word_guess)
                valid_input = True
            except WordleValidationError as e:
                print(str(e))
                valid_input = False
                continue

            try:
                matching = input('Enter matching pattern (GG_Y__):').lower()
                ws.validate_input('^[gy_]{5}$', matching)
                valid_input = True
            except WordleValidationError as e:
                print(str(e))
                valid_input = False

        ws.filter_words(word_guess, matching)
        
        sorted_freq = dict(sorted(ws.possible_words.items(), key = lambda x: x[1], reverse = True)[:10])

        for k, v in sorted_freq.items():
            print('{}\t\t{}'.format(k, v))


if __name__ == '__main__':
    main()
