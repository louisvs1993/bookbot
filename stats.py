def count_words(text):
    counter = len(text.split())
    return(f"Found {counter} total words")

def number_of_each_character(text):
    number_of_character = {}
    character_list = []
    for c in text:
        if c.lower() in number_of_character:
            number_of_character[c.lower()] += 1
        else:
            number_of_character[c.lower()] = 1

    for key, value in number_of_character.items():
        if key.isalpha():
            character_list.append({"character": key, "count": value})
    return character_list

def sort_on(dict):
    return dict['count']

def sort_dictiornary(dictonary):
    dictonary.sort(reverse=True, key=sort_on)
    return dictonary