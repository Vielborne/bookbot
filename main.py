import sys

from stats import get_num_characters, get_num_words, sort_character_list


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 1:
        file_path = sys.argv[1]
        file_contents = get_book_text(file_path)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")

        print(f"Found {get_num_words(file_contents)} total words")

        print("--------- Character Count -------")

        character_dict = get_num_characters(file_contents)
        character_list = sort_character_list(character_dict)
        for dict in character_list:
            print(f"{dict['char']}: {dict['num']}")

        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
