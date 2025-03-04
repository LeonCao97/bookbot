def get_book_text(file_path):
    with open(file_path) as f:
        results_string = f.read()
        results_list = results_string.split()
    return f"{len(results_list)} words found in the document."

def main():
    print(get_book_text("books/frankenstein.txt"))


main()