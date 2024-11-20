with open('books.txt', 'r', encoding='utf-8') as f:
    f.seek(55)
    print(f.read(26))
# "Преступление и наказание"