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


def sort_character_list(character_dict):
    character_list = []
    for key in character_dict:
        new_character_dict = {}
        new_character_dict["char"] = key
        new_character_dict["num"] = character_dict[key]
        character_list.append(new_character_dict)
        character_list.sort(reverse=True, key=sort_on)
    return character_list


def sort_on(character_list):
    return character_list["num"]
