def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words)
    count_characters(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_results = {}
    
    
    text_lower = text.lower()
    for character in text_lower:
        if not(character in character_results):
            character_results[character] = text_lower.count(character)
    print(character_results)


main()