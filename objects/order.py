class order :
    from objects.product import product
    def __init__(self,orderID,orderDATE):
        self.orderID = orderID
        self.orderDATE = orderDATE

    def __str__(self):
        return " ID: "+self.orderID+" Date: " + self.orderDATE