class customer :
    def __init__(self,customerID,customerNAME):
        self.customerID = customerID
        self.customerNAME = customerNAME

    def __str__(self):
        return " ID: "+str(self.customerID)+" Name: "+self.customerNAME