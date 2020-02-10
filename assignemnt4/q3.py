#Create a class book  with a parameterized constructor   having Title, Book Publisher, Author .
#Write a method to display book details
#Create emply list and add objects of book in the list
#hint Use for loop,append
#booklist=[]
class book:
    title=''
    book=''
    author=''
    def __init__(self,title,bookpublisher,author):
        self.title=title
        self.bookpublisher=bookpublisher
        self.author=author
    def display(self):
        print(self.title,self.bookpublisher,self.author)

limit=int(input("enter the how many books "))
booklist=[]
for i in range(1,limit+1,1):
    title=input("enter the title")
    bookpublisher=input("enter the book")
    author=input("enter the author")
    print(i)
    obj=book(title,bookpublisher,author)
    booklist.append(obj)

   #obj.display()
for i in booklist:
    i.display()




