from stats import get_book_text
from stats import word_counter
from stats import char_counter

word_count = word_counter(get_book_text("books/frankenstein.txt"))
print(f'Found {word_count} total words')
dict_count = char_counter(get_book_text("books/frankenstein.txt"))
print(dict_count)

