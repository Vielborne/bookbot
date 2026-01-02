def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words


def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    print(f"Found {get_num_words(file_contents)} total words")


main()
