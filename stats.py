def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_chars(book_text):
    chars = {}
        
    for char in book_text:
        if char.lower() not in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
    
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    sorted_chars = []
    for k, v in chars.items():
        new_dict = {"char": k, "num": v}
        sorted_chars.append(new_dict)
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars