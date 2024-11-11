def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words)

    final_list = make_list(count_characters(text))
    final_list.sort(reverse=True, key=sort_on)
    print_results(final_list, num_words, book_path)  


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
    return character_results

def make_list(dictionary_results):
    results_list = []
    
    for key, value in dictionary_results.items():
        if key in "abcdefghijklmnopqrstuvwxyz":
            dictionary_entry = {}
            dictionary_entry["name"] = key
            dictionary_entry["num"] = value
            results_list.append(dictionary_entry)  
    return results_list

def sort_on(dict):
    return dict["num"]

def print_results(results, count, bookPath):
    print(f"--- Begin report of {bookPath} ---")
    print(f"{count} words found in the document")
    for entries in results:
        print(f"The \'{entries["name"]}\' was found {entries["num"]} times")
    print("--- End report ---")    
main()