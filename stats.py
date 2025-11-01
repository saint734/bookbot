import io

def get_book_text(filepath:str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(book:str) -> int:
    word_count = len(book.split())
    return word_count

def char_counter(book:str) -> dict:
    counts = {}

    for i in range(len(book)):
        if book[i]:
            counts[book[i].lower()] = 1 + counts.get(book[i].lower(),0)
    return counts

def dict_sort(characters:dict) -> list:
    sorted_dict = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    # Got help here: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    for i in sorted_dict:
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")
