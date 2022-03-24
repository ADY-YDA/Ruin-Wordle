#sgb-words.txt from https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

import string

def load_words():
    file_to_open = 'sgb-words.txt'
    with open(file_to_open) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

#there's 5757 words in the list
def count_words():
    words = load_words()
    num = 0
    print(words[0])
    print(words[5756])
    for i in range(len(words)):
        num += 1
    print(num)

# count_words()

def alphabet_ranking():
    alpabet = dict.fromkeys(string.ascii_lowercase, 0)


"""
ideas for how to create Ruin Wordle

ordering/searching/filtering method:
    binary search tree (5757 words, can be filtered) ranked by how likely the word
    is likely going to be correct
    state space search (as in each word is placed in a group)

ranking: contains common letters, and letters in common spaces
higher chace of hit + faster filtering if removing large chunks

need functions for filtering words based on:
    whether letter is contained
    letter NOT at a position
    letter at a position
    word not recognized

interface:
    tells user which word to try
    options for inputting info based on Wordle response
        which letters are not included
        which letters are included but not in last tried position
        which letters are in correct position
        not recognized as a usable word (maybe have another .txt file that will delete words from future consideration as well)

other possible ideas for future:
    better list of 5 letter words (too many, and a few that probably aren't recognized as words)
    directly using word list from Wordle? Need to find how to get it
"""
