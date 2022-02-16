
class RetailItem:

    def __init__(self, desc, units, price):
        self.__desc = desc
        self.__units = units
        self.__price = price


    def set_desc(self, desc):
        self.__desc = desc

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    
    def get_desc(self):
        return self.__desc

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    def __str__(self):
        return '\nThe description is '+ self.__desc + '\nThe number of units in inventory is ' + str(self.__units) + '\nThe price for each '+self.__desc+' is ' + str(self.__price)


