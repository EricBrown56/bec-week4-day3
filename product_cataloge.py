'''Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.

Task 1: Create Base Product Class

Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
Expected Outcome: A Product class that can hold general information about a product and display it.

Task 2: Implement Subclasses for Specific Products

(ONLY BOOK SUBCLASS REQUIRED)

Create subclasses Book, Electronic, and Clothing that inherit from Product.
Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

Task 3: Override Display Method in Subclasses

Override the method to display product information in each subclass to include specific attributes.
For example, the Book class should display the author, Electronic should display specs, etc.
Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.

Task 4: Test Product Catalog Functionality

Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.
'''

class Product:
    '''Constructor and common attributes'''
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    

    def display_info(self):
        '''General method to display product info'''
        print(f"The current product is a {self.name} with a product id of {self.product_id}, which is selling for ${self.price} ")
        

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        '''Overridden method for books'''
        print(f"The current book is {self.name} written by {self.author}. Its product id is {self.product_id} and it is selling for ${self.price}")

# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()

class Electronics(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        '''Overridden method for electronics'''
        print(f"This electronic is a {self.name}, its specs are {self.specs} with a product id of {self.product_id} and is selling for ${self.price}")

my_tv = Electronics("TV324", "MegaVision TV", 988.85, "80 inch flat screen television")
my_tv.display_info()