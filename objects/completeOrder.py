class completeOrder :
    from objects.product import product
    def __init__(self,orderID,orderQUANTITY,orderDATE, product, products=[]):
        self.orderID = orderID
        self.orderQUANTITY= orderQUANTITY
        self.orderDATE = orderDATE
        self.products=products
        self.products.append(product)

    def addProduct(self,item):
        self.products.append(item)

    def __str__(self):
        return " ID: "+self.orderID+" Quantity : "+self.orderQUANTITY+ " Date: " + self.orderDATE + " Product/Products: "+str(self.products)