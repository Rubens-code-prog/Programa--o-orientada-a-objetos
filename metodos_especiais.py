class book(object):
    def __init__(self, title, author, pages):
        print('a book is created')
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return 'title:%s , author:%s , pages:%s ' %(self.title, self.author, self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('a book is destroyed')

book = book('curso de python', 'rodrigo tadewald', 159)
# métodos especiais
print(book)
print(len(book))
del book