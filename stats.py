def get_book_text(file_path):
    print(file_path)
    with open(file_path) as f:
        results_string = f.read()
        results_list = results_string.split()
    return f"Found {len(results_list)} total words"

def count_characters(inp):
    print(get_book_text(inp[1]))
    char_count = {}
    with open(inp[1]) as f:
        results_string = f.read()
        results_string_lower = results_string.lower()
        for char in results_string_lower:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] = char_count[char] + 1
        print(char_count)
    sorted_count(char_count)

def sort_on(dict):
    return dict["num"]

def sorted_count(char_dict):
    char_final_list = []
    for entry in char_dict:
        num = char_dict[entry]
        temp_entry = {'character': entry, 'num': num}


        char_final_list.append(temp_entry)
    

    char_final_list.sort(reverse = True, key = sort_on)
    for entry in char_final_list:
        print(f"{entry['character']}: {entry['num']}")
