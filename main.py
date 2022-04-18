import re
not_present_letters = []



class WordleSolver:

    absent_letters = []
    possible_words = []

    def __init__(filename):
        with open(filename) as f:
            self.possible_words = [line.lower().strip() for line in f.readlines()]

    def filter_words(self):
        pass

    def add_to_absent_letters(self, letter_list):
        for letter in letter_list:
            absent_letters.append(letter)

    def contains_absent_letters(self, word):
        for letter in absent_letters:
            if letter in word:
                return False
        return True





# --- Semi-working script based approach below

def read_word_list(filename):
    with open(filename) as f:
        wl = [l.lower().strip() for l in f.readlines()]
    return wl

def find_all(s_str, c):
    cursor = 0
    matched_indexes = []
    while cursor < len(s_str):
        next_index = s_str.find(c, cursor)
        print(next_index)
        if next_index == -1:
            break
        matched_indexes.append(next_index)
        cursor = next_index + 1
    return matched_indexes    

def contains_bad_letters(bad_letters, word):
    for bl in bad_letters:
        if bl in word:
            return True
    return False

def filter_word_list(possible_words, guess, matching):
    global not_present_letters
    filtered_words = possible_words.copy()
    for index, symbol in enumerate(matching):
        if symbol == '_':
            not_present_letters.append(guess[index])

    # TODO Wrap this in a function so we can return out of this loop
    for pw in possible_words:
        if contains_bad_letters(not_present_letters, pw):
            filtered_words.remove(pw)
            continue 

        # TODO Deal with edge case of HELLO - l in 3rd letter would be green, l in 4th would be yello
        for index, letter in enumerate(pw):
            
            symbol = matching[index]
            guessed_letter = guess[index]
            if symbol == 'y':
                if guessed_letter not in pw or letter == guessed_letter:
                    try:
                        filtered_words.remove(pw)
                    except:
                        pass
            elif symbol == 'g':
                if letter != guessed_letter:
                    try:
                        filtered_words.remove(pw)
                    except:
                        pass
    return filtered_words

def main():

    possible_words = read_word_list('words.txt')

    while len(possible_words) > 1:

        # TODO: Wrap in try / except blocks to get valid input
        word_guess = input('Enter guessed word: ').lower()
        matching = input('Enter matching pattern (GG_Y__):').lower()

        print(word_guess, matching)
        # TODO Check if word is a valid word

        possible_words = filter_word_list(possible_words, word_guess, matching)
        
        print(possible_words)

if __name__ == '__main__':
    main()
