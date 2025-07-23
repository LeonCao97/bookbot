def word_count(book_text):
    list_words = book_text.split()
    num_words = len(list_words)
    print(f"Found {num_words} total words")

def character_count(book_text):
    str_book_lower = book_text.lower()
    character_stats = {}
    for char in str_book_lower:
        if char not in character_stats:
            character_stats[char] = 1
        else:
            character_stats[char] += 1
    print(character_stats)
    return(character_stats)

def final_results(initial_dict):
    final_list = []
    for key in initial_dict:
        individual_entry = {}
        individual_entry["char"] = key
        individual_entry["num"] = initial_dict[key]
        final_list.append(individual_entry)
    #print(final_list)
    final_list.sort(reverse=True, key=sort_on)
    return(final_list)

    

def sort_on(items):
    return items["num"]



