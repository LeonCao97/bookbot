def get_book_text(file_path):
    with open(file_path) as f:
        results_string = f.read()

    return results_string

def main():
    print(get_book_text("books/frankenstein.txt"))


main()