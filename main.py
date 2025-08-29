import sys
from stats import get_num_words 
from stats import get_num_characters 
from stats import sort_on

print("============ BOOKBOT ============")

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    
    
    print("Analyzing book found at path:", sys.argv[1])
    print("----------- Word Count ----------")

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_num_characters(book_text)
    sorted_char_count = sort_on(char_count)
    for char_count in sorted_char_count:
        print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")

main()
