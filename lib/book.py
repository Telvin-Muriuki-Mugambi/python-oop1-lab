#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self,value):
        if type (value) is int:
            self._page_count = value
        else:
            print("page_count must be an integer")
        
    def turn_page(self):
        print ("Flipping the page...wow, you read fast!")

    def __repr__(self):
        return f"{self.title} has {self.page_count} pages"


book1 = Book("Atomic Habits",232)
print(book1)
book1.turn_page()

    
        