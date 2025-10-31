def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
print(get_book_text("books/frankenstein.txt"))
