class product :
    def __init__(self,productID,productNAME,price,productCATEGORY,productWEB):
        self.productID = productID
        self.productNAME= productNAME
        self.price= price
        self.productCATEGORY= productCATEGORY 
        self.productWEB=productWEB
        
    def __str__(self):
        return " ID: "+self.productID+" Product Name : "+self.productNAME+ " price: " + self.price + " Category: "+self.productCATEGORY + " URL: "+self.productWEB