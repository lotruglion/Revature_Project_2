class payment:
    def __init__(self,paymentID,paymentTYPE,paymentSUCCESS,paymentFAILreason) :
        self.paymentTYPE= paymentTYPE
        self.paymentID= paymentID
        self.paymentSUCCESS= paymentSUCCESS
        self.paymentFAILreason=paymentFAILreason

    def __str__(self):
        return " ID: "+self.paymentID+" Payment Type : "+self.paymentTYPE+ " Payment Succcess: " + self.paymentSUCCESS + " Fail Reason :"+self.paymentFAILreason