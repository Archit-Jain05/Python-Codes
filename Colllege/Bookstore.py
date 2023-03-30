class BookStore:

    TotalBooks=0
    def __init__(self,title,author,qty,price):
        print("Welcome to __init__() constructor")
        self.title=title
        self.author=author
        self.qty=qty
        self.price=price
        BookStore.TotalBooks+=1
        
    def getBook(self):
        print("Title = ",self.title)
        print("Author = ",self.author)
        print("Quantity = ",self.qty)
        print("Price = ",self.price)

    def valuation(self):
        return self.qty*self.price
    
    def update_qty(self):
        print("Enter the quantity added: ")
        add=int(input())
        self.qty+=+add

    def update_price(self):
        print("Enter the increase percentage: ")
        per=float(input())
        self.price+=self.price*per/100

b1=BookStore("Wimpy","JK Rowling",10,1200)

b1.getBook()
print("Valuation of B1 = ",b1.valuation())
print("Number of Books = ",BookStore.TotalBooks)

b1.update_qty()
b1.getBook()
b1.update_price()
b1.getBook()
