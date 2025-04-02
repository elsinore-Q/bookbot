import sys
from stats import count_words, count_characters, sort_character_counts

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    print(f"""============ BOOKBOT ============ 
Analyzing book found at {filepath}...""")

    num_words = count_words(text)
    print(f"""----------- Word Count ----------
Found {num_words} total words""")

    char_counts = count_characters(text)
    sorted_characters = sort_character_counts(char_counts)

    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['character']}: {item['count']}")
    print("============= END ===============")
main()
