class Dataplan():
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__speed = ""
        self.__pricepermonth = 0



    def getDataplanInfo_id(self):
            return self.__id

    def getDataplanInfo_name(self):
            return self.__name

    def getDataplanInfo_speed(self):
            return self.__speed

    def getDataplanInfo_pricepermonth(self):
            return self.__pricepermonth


    def setDataplanInfo(self, id, name, speed, pricepermonth):
        self.__id = id
        self.__name = name
        self.__speed = speed
        self.__pricepermonth= pricepermonth

