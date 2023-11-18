def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = count_letters(text)
    print(letter_count)
    
    

def get_word_count(text):
        words = text.split()
        return len(words)   

def get_book_text(book_path):
        with open(book_path) as f:
            text = f.read()
            return text    

def count_letters(text):
    letter_count = {}
    l_text = text.lower()
    
    for let in l_text:
          letter_count[let] = letter_count.get(let,0)+1
    return letter_count

   


main()