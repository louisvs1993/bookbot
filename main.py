from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    print_report(filepath)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def print_report(filepath):
    sorted_dictionary = sort_dictiornary(number_of_each_character(get_book_text(filepath)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(count_words(get_book_text(filepath)))
    print("--------- Character Count -------")
    for key_value in sorted_dictionary:
        print(f"{key_value['character']}: {key_value['count']}")
    print("============= END ===============")

    
main()