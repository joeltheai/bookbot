from stats import get_book_text, count_characters
import sys

def count_words(book_text):
    return len(book_text.split())

def main():
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    try:
        frankenstein_text = get_book_text(book_path)
        num_words = count_words(frankenstein_text)
        characters = count_characters(frankenstein_text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char, count in characters.items():
            print(f"{char}: {count}")
        print("============ END ===============")
        
    except FileNotFoundError:
        print(f"Error: Book file '{book_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading book: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()