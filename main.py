def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = count_letters(text)

    sorted_list = dict_to_sorted(letter_count)
    
    print(f"--- Begin report of {book_path}---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_list:
        if not item["let"].isalpha():
            continue
        print(f"The '{item['let']}' character was found {item['num']} times")

    print("--- End report---")

   

def get_book_text(book_path):
    with open(book_path) as f:
        text = f.read()
        return text

def get_word_count(text):
    words = text.split()
    return len(words)   

def count_letters(text):
    letter_count = {}
    l_text = text.lower()
    for let in l_text:
          letter_count[let] = letter_count.get(let,0)+1
    return letter_count

def sort_on(d):
    return d["num"]

def dict_to_sorted(letter_count):
    sorted_list = []
    for letter in letter_count:
        sorted_list.append({"let": letter, "num": letter_count[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


    


main()