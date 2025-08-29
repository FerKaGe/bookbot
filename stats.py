def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_num_characters(text: str) -> dict:
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(char_count: dict) -> list:
    def num(d):
        return d["num"]
    dicts = []
    for char in char_count:
        if char.isalpha():
            dicts.append({"char": char, "num": char_count[char]})
    dicts.sort(reverse=True, key=num)
    return dicts