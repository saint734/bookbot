from stats import get_book_text
from stats import word_counter
from stats import char_counter
from stats import dict_sort
import sys 

filepath = sys.argv
print("=" * 12, "BOOKBOT", "=" * 12)
try: 
    print(f"Analyzing book found at {filepath[1]}...")
except IndexError as e:
    print("Missing a second argument")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
print("-" * 10, "Word Count", "-" * 11)

word_count = word_counter(get_book_text(filepath[1]))
print(f"Found {word_count} total words")
print("-" * 8, "Character Count", "-" * 8)

dict_count = char_counter(get_book_text(filepath[1]))
#print(dict_count)
#sorted_dict = dict_sort(dict_count)
print(dict_sort(dict_count))
print("=" * 14, "END", "=" * 14)
