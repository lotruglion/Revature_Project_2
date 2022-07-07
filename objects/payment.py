class payment:
    def __init__(self,paymentID,paymentTYPE,paymentSUCCESS,paymentFAIL,paymentFAILreason) :
        self.paymentTYPE= paymentTYPE
        self.paymentID= paymentID
        self.paymentSUCCESS= paymentSUCCESS
        self.paymentFAIL = paymentFAIL
        self.paymentFAILreason=paymentFAILreason