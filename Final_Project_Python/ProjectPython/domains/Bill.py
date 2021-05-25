class Bill():
    def __init__(self):
        self.__id = 0
        self.__customerid = 0
        self.__dataplanid = 0
        self.__registrationdate = ""
        self.__duration = 0
        self.__totalamount = 0


    def getBillInfo_Bill_id(self):
        return self.__id
    def getBillInfo_Bill_Customerid(self):
        return self.__customerid
    def getBillInfo_Bill_Dataplanid(self):
        return self.__dataplanid
    def getBillInfo_Bill_RegistrationDate(self):
        return self.__registrationdate
    def getBillInfo_Bill_Duration(self):
        return self.__duration
    def getBillInfo_Bill_Totalamount(self):
        return self.__totalamount

    def setBillInfor(self, id, customerid, dataplanid, registrationdate, duration, totalamount):
        self.__id = id
        self.__customerid = customerid
        self.__dataplanid = dataplanid
        self.__registrationdate = registrationdate
        self.__duration = duration
        self.__totalamount = totalamount


