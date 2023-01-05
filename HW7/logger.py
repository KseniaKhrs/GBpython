def read_phone_book():
    with open('book.txt', 'r', encoding='utf-8') as b:
            text = b.read()
    return dict(subString.split(': ') for subString in text.split('; '))

def add_new_contact(name, number):
    with open('book.txt', 'a', encoding='utf-8') as b:
            b.write(f'; {name}: {number}')
