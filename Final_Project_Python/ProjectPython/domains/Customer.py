class Customer():

    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__phoneNumber = 0
        self.__address = ""


    def getCustomerInfo_id(self):
        return self.__id
    def getCustomerInfo_name(self):
        return self.__name
    def getCustomerInfo_phoneNumber(self):
        return self.__phoneNumber
    def getCustomerInfo_address(self):
        return self.__address


    def setCustomerInfo(self, id, name, phoneNumber, address):
        self.__id = id
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__address = address

