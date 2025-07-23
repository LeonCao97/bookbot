from stats import word_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents




def main():
    word_count(get_book_text("books/frankenstein.txt"))
    character_count(get_book_text("books/frankenstein.txt"))
    

main()