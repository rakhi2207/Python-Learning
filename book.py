class Book:
    def __init__(self,id,name,desc,isbn,page_count,issued,author,year):
        self.id=id
        self.name=name
        self.desc=desc
        self.isbn=isbn
        self.page_count=page_count
        self.issued=issued
        self.author=author
        self.year=year

    def to_dict(self):
        dict={
            "id":self.id,
            "name":self.name,
            "Description":self.desc,
            "isbn":self.isbn,
            "page_count":self.page_count,
            "issued":self.issued,
            "author":self.author,
            "year":self.year
        }
        return dict

