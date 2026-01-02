def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words


def get_num_characters(book_text):
    lower_cased_text = book_text.lower()
    num_words = lower_cased_text.split()
    character_dict = {}
    for word in num_words:
        for ch in word:
            if ch in character_dict:
                character_dict[ch] += 1
            else:
                character_dict[ch] = 1
    return character_dict
