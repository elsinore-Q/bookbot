def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_counts(char_count):
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():
            sorted_list.append({"character": char, "count": count})
    sorted_list.sort(key=lambda item: item["count"], reverse=True)
    return sorted_list
