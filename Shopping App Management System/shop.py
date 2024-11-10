class Shop:
    def __init__(self,name):
        self.name = name
        self.products = []
        self.sellers = []
        self.customers = []
    def addSeller(self,seller):
        self.sellers.append(seller)
    def addCustomer(self,customer):
        self.customers.append(customer)
    def showProduct(self):
        print("\tProducts\n")
        print("Name\tPrice\tQuantity")
        for item in self.products:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
    
    def removeProduct(self,productName):
        flag = False
        for item in self.products:
            if item.name.lower()==productName.lower():
                self.products.remove(item)
                print(f"{productName} is removed from the shop")
                flag = True
                break
        if flag == False:
            print(f"product named {productName} not found in the shop")

    def findProduct(self,productName):
        for item in self.products:
            if item.name.lower() == productName.lower():
                return item
        return None