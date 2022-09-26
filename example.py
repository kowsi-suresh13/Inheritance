class Books:
    def __init__(self,series_no,Title,book_id):
        self.series_no=series_no
        self.Title=Title
        self.book_id=book_id
        

class story_books(Books):
    def __init__(self,series_no,Title,book_id,Author):
        super().__init__(series_no,Title,book_id)
        self.Author=Author

class tech_books(story_books):
    def __init__(self,series_no,Title,book_id,Author,Publisher):
        super().__init__(series_no,Title,book_id,Author)
        self.Publisher=Publisher

class Novels(Books):
    def __init__(self,series_no,Title,book_id,Parts):
        super().__init__(series_no,Title,book_id)
        self.Parts=Parts

class book_name(Books):
    def __init__(self,series_no,Title,book_id,b_names=[]):
        super().__init__(series_no,Title,book_id)
        self.b_names=b_names

    def show_names(self):
        for name in self.b_names:
             print(name.Title)
             
b1=tech_books(1,"Electronic Devices",5667,"Suresh","Monish")
b2=story_books(2,"The jungle book",6787,"Kowsi")
b3=Novels(4,"The Alchemist",8786,23)
n=book_name(5,"Book Names",6778,[b1,b2,b3])
print(n.Title)
n.show_names()
