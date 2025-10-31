def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(book:str) -> int:
    word_count = len(book.split())
    return word_count

