from user import Seller,Customer
from shop import Shop
from product import Product
import random
swapno = Shop('Swapno')
user = None

def seller():
    print("Login as a seller :")
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    sell = Seller(name,email,password)
    swapno.addSeller(sell)
    id = random.randint(111111,999999)
    print(f"Welcome Seller id - {id}")
    while True:
        print()
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Products")
        print("4. Exit")
        option = int(input("Enter your option : "))
        if option == 1:
            name = input("Product name : ")
            price = int(input("Product price : "))
            quantity = int(input("Product quantity : "))
            sell.addProduct(swapno,Product(name,price,quantity))
        elif option == 2:
            name = input("Product name : ")
            sell.removeProduct(swapno,name)
        elif option == 3:
            sell.showProduct(swapno)
        elif option == 4:
            break
        else:
            print("Wrong optin")

def customer():
    print("Login as a customer :")
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    cus = Customer(name,email,password)
    swapno.addSeller(cus)
    id = random.randint(111111,999999)
    print(f"Welcome {name}")
    while True:
        print()
        print("1. View Products")
        print("2. Add Product on Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        option = int(input("Enter your option : "))
        if option == 1:
            cus.showProduct(swapno)
        elif option == 2:
            name = input("Product name : ")
            quantity = int(input("Product quantity : "))
            cus.addToCart(swapno,name,quantity)
        elif option == 3:
            name = input("Product name : ")
            cus.removeFromCart(name)
        elif option == 4:
            cus.showCart()
        elif option == 5:
            cus.payBill()
        elif option == 6:
            break
        else:
            print("Wrong optin")

while True:
    if user == None:
        print("1. Seller")
        print("2. Customer")
        print("3. Exit")

        option = int(input("Enter your option : "))
        if option == 1:
            seller()
        elif option == 2:
            customer()
        elif option == 3:
            break
        else:
            print("Wrong optin")
        
