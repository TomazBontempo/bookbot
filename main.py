
import sys
from stats import word_count
from stats import char_count
from stats import le_sorter


def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text



def main():
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        file_path = sys.argv[1]
        book = get_book_text(file_path)
        chars = char_count(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        word_count(book)  
        print("--------- Character Count -------")
        le_sorter(chars)
        print("============= END ===============")
        sys.exit(0)  # Exit with a success code
    else:
        print("No arguments provided - Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with an error code


main()


