from stats import get_num_characters, get_num_words


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    print(f"Found {get_num_words(file_contents)} total words")
    print(get_num_characters(file_contents))


main()
