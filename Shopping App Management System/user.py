from product import Product
from shop import Shop
class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password


class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def addProduct(self,shop,product):
        flag = False
        for item in shop.products:
            if item.name.lower() == product.name.lower():
                item.quantity += product.quantity
                flag = True
                break
        if flag == False:
            shop.products.append(product)
    def removeProduct(self,shop,productName):
        shop.removeProduct(productName)
    def showProduct(self,shop):
        shop.showProduct()

class Customer(User):
    def __init__(self, name, email, password):
        self.cart = []
        self.total = 0
        super().__init__(name, email, password)
    def showProduct(self,shop):
        shop.showProduct()
    def addToCart(self,shop,productName,quantity):
        item = shop.findProduct(productName)
        if item == None:
            print("Product is not available at this moment")
        else :
            if item.quantity<quantity:
                print("Insufficient Quantity")
            else:
                self.cart.append(Product(item.name,item.price,quantity))
                self.total += item.price*quantity
                print(f"{quantity} pieces {productName} added to cart")
                item.quantity -= quantity
                if item.quantity ==0 :
                    shop.removeProduct(productName)
    def removeFromCart(self,productName):
        flag = False
        for item in self.cart:
            if item.name.lower() == productName:
                self.total -= (item.price*item.quantity)
                
                self.cart.remove(item)
                flag = True
                print("Item is removed from cart")
                break
        if flag == False:
            print("Item is not in the cart")
    def showCart(self):
        print("\tCart\n")
        print("Name\tPrice\tQuantity")
        for item in self.cart:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
        print(f"Total price : {self.total}")
    
    def payBill(self):
        print(f"Total {self.total} paid successfull")
        self.total = 0
        self.cart = []
    