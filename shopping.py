from datetime import datetime
import os

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

class Food(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        #check whether the procuct already exists in the cart
        for i, (item, qty) in enumerate(self.items):
            if item.name == product.name:
                self.items[i] = (item, qty + quantity)
                return
        self.items.append((product, quantity))

    def remove_item(self, product_name):
        self.items = [item for item in self.items if item[0].name != product_name]

    def view_cart(self):
        print("Items in your cart:")
        print("-" * 30)
        for product, quantity in self.items:
            print(f"{product.name} - ${product.price} x {quantity}")
        input("press Enter to continue...")

    def clear_cart(self):
        self.items = []
    
    def place_order(self, name, number, invoice_name):
        invoice_name += ".txt"
        with open(invoice_name, "w") as f:
            f.write("\t" *5 + "Generated Invoice the cart\n\n")
            f.write(f"Customer Name: {name}\n")
            f.write(f"Customer Number: {number}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("Items:\n")
            total = 0
            for product, quantity in self.items:
                f.write(f"{product.name} x {quantity}".ljust(40,' ')  + f" : ${product.price * quantity} \n")
                total += product.price * quantity
            f.write("\n" + "-" * 80 + "\n")
            f.write("Total Amount".ljust(40,' ') + f" : ${total}"+ "\n")
            saved_path = os.path.abspath(invoice_name)
        return saved_path
    

def ShowInfo():
    text = "> Start the Shopping <"
    print(text.center(100, "-"))
    option_list = ["Add item to cart", "Remove item from cart", "View cart", "update item Quantity", "Clear cart", "Place Order", "Exit"]
    for i, option in enumerate(option_list, start=1):
        print(' '*40, end='')
        print(f"{i}. {option}")
    option = int(input("Enter your choice (1-7): "))
    return option

def validate_name_number(name, number):
    # name: alphabetic + spaces only, min 2 chars
    if not all(c.isalpha() or c.isspace() for c in name) or len(name.strip()) < 2:
        return False
    # number: digits only, exactly 10 chars with optional 0 or 91 at start1
    if number.startswith('0') or number.startswith('91'):
        if not number.isdigit() or len(number) != 12:
            return False
    elif not number.isdigit() or len(number) != 10:
        return False
    return True
# ...existing code...

if __name__ == "__main__":
    invoice_path = ''
    products = [
        Electronics("Laptop", 40000, 2),
        Electronics("Headphones", 3000, 1),
        Electronics("SamsungS22", 82000, 1),
        Clothing("Shirt", 500, "M"),
        Clothing("Pant", 1200, "L"),
        Food("Apple", 50, "2024-12-01"),
        Food("Banana", 30, "2024-06-15"),
        Food("Pappaya", 40, "2024-06-10")
    ]
    cart = Cart()
    while True:
        option = ShowInfo()
        if option == 1:
            print("Available Products to add to cart:")
            for i, product in enumerate(products, start=1):
                print(' '*25, end='')
                print(f"{i}. {product.name} - ${product.price}")
            choice = int(input("Select a product to add to cart (1-8): "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(products[choice - 1], quantity)
            cart.view_cart()
        elif option == 2:
            cart.view_cart()
            product_name = input("Enter the name of the product to remove from cart: ")
            cart.remove_item(product_name)
            cart.view_cart()
        elif option == 3:
            cart.view_cart()
        elif option == 4:
            cart.view_cart()
            product_name = input("Enter the name of the product to update quantity: ")
            quantity = int(input("Enter new quantity: "))
            cart.remove_item(product_name)
            for product in products:
                if product.name == product_name:
                    cart.add_item(product, quantity)
                else:
                    print("Product not found in cart.")
            cart.view_cart()
        elif option == 5:
            cart.clear_cart()
            print("Cart cleared.")
        elif option == 6:
            name = input("Enter your name: ")
            number = input("Enter your number: ")
            validate = validate_name_number(name, number)
            if not validate:
                print("Invalid name or number. Please try again.")
                continue
            invoice_name = input("Enter invoice file name: ")
            invoice_path = cart.place_order(name, number, invoice_name)
            print("Order placed successfully!")
            print("Thank you for shopping! Please fimnd the invoice at "+invoice_path)
            break
        elif option == 7:
            print("Exiting the program. Thank you for shopping!")
            break

