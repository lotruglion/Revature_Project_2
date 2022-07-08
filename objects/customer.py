class customer :
    def __init__(self,customerID,customerNAME,customerCOUNTRY,customerCITY):
        self.customerID = customerID
        self.customerNAME = customerNAME
        self.customerCOUNTRY = customerCOUNTRY
        self.customerCITY = customerCITY

    def __str__(self):
        return " ID: "+str(self.customerID)+" Name: "+self.customerNAME