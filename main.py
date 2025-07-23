from stats import word_count, character_count, final_results
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents





def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        word_count(get_book_text(sys.argv[1]))
        character_count(get_book_text(sys.argv[1]))
        final_entries = final_results(character_count(get_book_text(sys.argv[1])))
        print("----Character Count-----")
        for entry in final_entries:
            print(f"{entry["char"]}: {entry["num"]}")


main()