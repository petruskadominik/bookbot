import string
def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    word_count = count_words(path_to_book)
    character_count = count_characters(path_to_book)
    print(text)
    print(word_count)
    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(path):
    word_count = 0
    with open(path) as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(path):
    character_count = dict([(chr(i),0) for i in range(97,123)])
    with open(path) as f:
        text = f.read()
    lowered_txt = text.lower()

    for c in lowered_txt:
        for char in character_count:
            if c == char:
               character_count[char] += 1
               
    return character_count


main()