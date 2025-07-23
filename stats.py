def word_count(book_text):
    list_words = book_text.split()
    num_words = len(list_words)
    print(f"{num_words} words found in the document")

def character_count(book_text):
    str_book_lower = book_text.lower()
    character_stats = {}
    for char in str_book_lower:
        if char not in character_stats:
            character_stats[char] = 1
        else:
            character_stats[char] += 1
    print(character_stats)
