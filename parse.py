#sgb-words.txt from https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

def load_words():
    file_to_open = 'sgb-words.txt'
    with open(file_to_open) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

#there's 5757 words in the list
def count_words():
    file_to_open = 'sgb-words.txt'
    with open(file_to_open) as word_file:
        valid_words = list(word_file.read().split())
    num = 0
    print(valid_words[0])
    print(valid_words[5756])
    for i in range(len(valid_words)):
        num += 1
    print(num)

count_words()
