
def get_book_text(file_path):
    with open(file_path, "r") as f:
        file_content = f.read()

    return file_content

def count_characters(book_text):
    characters = {}
    
    for char in book_text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)
    characters = {char:count for char, count in characters if char.isalpha()}

    return characters