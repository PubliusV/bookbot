def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    total_words = count_words(text)
    print(f"{total_words} words found in the document.\n")
    char_counts = count_characters(text)
    pretty_characters = []
    for k,v in char_counts.items():
        pretty_characters.append({"character":k,"value":v})

    pretty_characters.sort(reverse=True, key=sort_on)
    for item in pretty_characters:
        print(f"The '{item['character']}' character was found {item['value']} times.")
    print("--- End report ---")

def sort_on(dict):
    return dict["value"]

def count_characters(corpus:str):
    character_counts = {}
    lowered_str = corpus.lower()
    for char in lowered_str:
        if not char.isalpha():
            continue
        if char in character_counts.keys():
            character_counts[char] += 1
        else:
            character_counts[char]=1
    return character_counts

def count_words(corpus:str):
    words = corpus.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()