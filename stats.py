def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(book:str) -> int:
    word_count = len(book.split())
    return word_count

def char_counter(book:str) -> dict:
    counts = {}

    for i in range(len(book)):
        counts[book[i].lower()] = 1 + counts.get(book[i].lower(),0)
    return counts
