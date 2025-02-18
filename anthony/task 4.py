class Book:
    def __init__(self, title, author, year_published, editions=None):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.editions = editions if editions else []  
        
       
        if self.year_published < 1000 or self.year_published > 2025:
            raise ValueError("Invalid year of publication")

    def add_edition(self, edition):
        """Method to add an edition to the book."""
        self.editions.append(edition)

    def describe(self):
        """Method to describe the book details."""
        editions_str = ", ".join(self.editions) if self.editions else "No editions available"
        print(f"Book Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}\nEditions: {editions_str}\n")

    def __str__(self):
        """Override string representation to make it more readable."""
        return f"'{self.title}' by {self.author} ({self.year_published})"


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, ["First Edition", "Collector's Edition"])
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960, ["50th Anniversary Edition"])


book2.add_edition("Special Edition")


print(book1)
book1.describe()
print(book2)
book2.describe()
print(book3)
book3.describe()