def word_count(text):
    words = text.split()
    count =  len(words)
    return print(f"Found {count} total words") 

def char_count(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars

def le_sorter(chars):
    dic_list = []
    for key, value in chars.items():
        new_dict = {"char": key, "count": value}  # Create the new dictionary
        dic_list.append(new_dict)  # Add it to the list
    dic_list.sort(reverse=True, key=lambda x: x["count"])  # Sort by count
    for d in dic_list:
        if d["char"].isalpha():  # Check if the character is alphabetical
            print(f"{d['char']}: {d['count']}")  # Print formatted string
    return None




