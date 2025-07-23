import sys
from stats import count_words, count_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as b:
        book = b.read()
        return book

def print_chars(sorted_chars):
    for dictionary in sorted_chars:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    

def main():
    
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    sorted_chars = sort_chars(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # print(char_count)
    # print(sorted_chars)
    print_chars(sorted_chars)
    print("============= END ===============")

main()