import re
import datetime
    # 1) Begins with 0 or 91
    # 2) Then contains 6,7, 8 or 9.
    # 3) Then contains 9 digits
Pattern = re.compile("(0|91)?[6-9][0-9]{9}$")
#phone_number_regex = r"^(?:\+91|0)?[1-9]\d{9}$"
name_pattern = re.compile(r"^[a-zA-Z\s]+$")

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Product(Item):
    TAX_RATE = 0.1  # 10% tax rate

    def __init__(self, name, price):
        super().__init__(name, price)

    def total_cost(self, quantity):
        total = self.price * quantity
        total_with_tax = total * (1 + Product.TAX_RATE)
        return total_with_tax


class Electronics(Item):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def __str__(self):
        return f"{super().__str__()}, Warranty: {self.warranty} months,"


class Clothing(Item):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"{super().__str__()}, Size: {self.size},"


class Food(Item):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{super().__str__()}, Expiry Date: {self.expiry_date},"


class shopping_cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item["product"].name == product.name:
                item["quantity"] += quantity
                print(f"{quantity} {product.name}(s) added to the cart.")
                return
                
        print("\n")
        print("Last added product to cart ", product,"quantity -",quantity)
        self.items.append({"product": product, "quantity": quantity, "price":product.price})
        

    def view_cart(self):
        cart_total_cost = 0
        if not self.items:
            print(f"Your cart is empty.")
            print(f"Total Cart Price: {cart_total_cost}")
        else:
            print("\n")
            print("Items in your cart:")
            for item in self.items:
                cart_total_cost += item['price'] * item['quantity']
                print(f"{item['product']} x {item['quantity']}")
            print(f"Total Cart Price: {cart_total_cost}")

    def update_quantity(self, product_name, new_quantity):
        for item in self.items:
            if item["product"].name == product_name:
                item["quantity"] = new_quantity
                print(f"Quantity of {product_name} updated to {new_quantity}.")
                return
        print(f"{product_name} not found in the cart.")


    def remove_item(self, product_name):
        for item in self.items:
            if item["product"].name == product_name:
                self.items.remove(item)
                print("\n")
                print(f"{product_name} removed from the cart.")
                return
        print(f"{product_name} not found in the cart.")


    def clear_cart(self):
        self.items = []
        print("Cart cleared.")
        
        
    @staticmethod
    def cust_name():
        while True:
            cust_name = input("Enter your name: ")
            if name_pattern.match(cust_name):
                return cust_name
            else:
                print("\n")
                print("In valid Name\nIt must start with A to Z or a to z follow with space.")
        
    @staticmethod
    def phone_num():
        while True:
            phone_num = input("Enter the Phone Number: ")
            if Pattern.match(phone_num):
                return phone_num
            else:
                print("\n")
                print("In valid Phone Number,\nIt must start with (0 or 91)\nstart with 6,7,8 or 9 and followed 9 digits)")


    def place_order(self, filename, cust_name, phone_num):
        if not self.items:
            print("Cannot place an order with an empty cart.")
            return

        total = 0
        invoice = 20*" "+"Generated Invoice the cart\n"
        invoice += f"\n"
        invoice += f"Customer Name: {cust_name}\n"
        invoice += f"Phone Number: {phone_num}\n"
        invoice += f"Date: {datetime.datetime.now()}\n"
        invoice += f"\n"
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total += Product.total_cost(product, quantity)
            invoice += f"{product.name} x {quantity}{10*' '}            : ${Product.total_cost(product, quantity)}\n"
        invoice += f"\n"
        invoice += f"----------------------------------------------------------\n"
        invoice += f"Total:{30*' '}${round(total, 3)}"

        with open(filename, "w") as file:
            file.write(invoice)

        print(f"Invoice generated and saved to {filename}")
        self.clear_cart()

def show_menu():
    print("\n-----------------------> Start the shopping <---------------------")
    print(20*" ","1. Add item to cart")
    print(20*" ","2. Remove item from cart")
    print(20*" ","3. View cart")
    print(20*" ","4. Update item quantity")
    print(20*" ","5. Clear cart")
    print(20*" ","6. Place order")
    print(20*" ","7. Exit")


# Sample usage
if __name__ == "__main__":

    # Creating some products bydefault
    laptop = Electronics("Laptop", 40000, 12)
    headphones = Electronics("Headphones", 3000, 6)
    phone = Electronics("SamsungS22", 82000, 18)
    shirt = Clothing("Shirt", 600, "Medium")
    pant = Clothing("Pant", 1200, "34")
    apple = Food("Apple", 50, "2024-04-30")
    banana = Food("Banana", 10, "2024-04-30")
    papaya = Food("Papaya", 60, "2024-04-30")

    # Initialize shopping cart
    cart = shopping_cart()

    # Menu loop
    while True:
        show_menu()
        #User choice to add products to cart
        user_choice = input("Enter your choice: ")

        #get the choice
        if user_choice == "1":
            print("\n")
            print("Available products to Add to cart :")
            print(20*" ","1. Laptop - 1N = 40000, Warranty: 12 months")
            print(20*" ","2. Headphones - 1N = 3000, Warranty: 6 months")
            print(20*" ","3. SamsungS22 - 1N = 82000, Warranty: 18 months")
            print(20*" ","4. Shirt - 1N = 600, Size: Medium")
            print(20*" ","5. Pant - 1N = 1200, Size: 34")
            print(20*" ","6. Apple - 1N = 50, Expiry Date: 2024-04-30")
            print(20*" ","7. Banana - 1N = 10, Expiry Date: 2024-04-30")
            print(20*" ","8. Papaya - 1N = 60, Expiry Date: 2024-04-30")
            #Take Inputs from user
            product_choice = input("Enter the product number from above : ")
            product_quantity = int(input("Enter the product quantity: "))

            if product_choice == "1":
                cart.add_item(laptop, product_quantity)
            elif product_choice == "2":
                cart.add_item(headphones, product_quantity)
            elif product_choice == "3":
                cart.add_item(phone, product_quantity)
            elif product_choice == "4":
                cart.add_item(shirt, product_quantity)
            elif product_choice == "5":
                cart.add_item(pant, product_quantity)
            elif product_choice == "6":
                cart.add_item(apple, product_quantity)
            elif product_choice == "7":
                cart.add_item(banana, product_quantity)
            elif product_choice == "8":
                cart.add_item(papaya, product_quantity)
            else:
                print("Invalid product number.")
        elif user_choice == "2":
            product_name = input("Enter the name of the product to remove: ")
            cart.remove_item(product_name)
        elif user_choice == "3":
            cart.view_cart()
        elif user_choice == "4":
            product_name = input("Enter the name of the product to update quantity: ")
            new_quantity = int(input("Enter the new quantity: "))
            cart.update_quantity(product_name, new_quantity)
        elif user_choice == "5":
            cart.clear_cart()
        elif user_choice == "6":
            cust_name = cart.cust_name()
            phone_num = cart.phone_num()
            file_name = input("Enter the filename for the invoice (e.g., invoice): ")
            if not file_name:
                print("\n")
                print("In valid File Name")
            else:
                print("Placing an order")
                cart.place_order(file_name+".txt", cust_name, phone_num)
        elif user_choice == "7":
            print("Logging off thank you. Visit Again!")
            break
        else:
            print("\n")
            print("Invalid choice. Please choose again.")