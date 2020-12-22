class AirCondition:
    def __init__(self, brand, temperature):
        self.brand = brand
        self.temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if 18 <= value <= 31:
            self.__temperature = value
        elif value < 18:
            self.__temperature = 18
        else:
            self.__temperature = 31


geli = AirCondition("格力", 15)
print(geli.temperature)
