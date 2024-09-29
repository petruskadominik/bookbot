def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    word_count = count_words(path_to_book)
    print(text)
    print(word_count)

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

main()