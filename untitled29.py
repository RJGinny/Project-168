#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:38:58 2022

@author: riddhiekajain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:18:26 2022

@author: riddhiekajain
"""

class Bookshelf:
    def __init__(self, name, author, price, publishing_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publishing_year= publishing_year
        
    def add_book(self):
            print(" Book Name: "+self.book_name)
            print("Book Author: "+self.book_author)
            print("Book Price: "+str(self.book_price))
            print("Publishing Year "+str(self.book_publishing_year))
            print("Book Added")
            
    def year_since_published(self):
        year_ago_published= 2022-self.book_publishing_year
        print("This book was published "+ str(year_ago_published)+" years ago")
        
book1 = Bookshelf("Diary of a Wimpy Kid","Jeff Kinney", 350, 2008)
book1.add_book()
book1.year_since_published()

book2 = Bookshelf("Harry Potter and the philosophers stone","J.K Rowling", 350, 1991)
book2.add_book()
book2.year_since_published()
