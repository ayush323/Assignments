class Car:
    def __init__(self, speed, regularPrice, color):
        self.speed = speed
        self.regularPrice = regularPrice
        self. color = color

    def doublegetSalePrice(self):
        pass

class Truck(Car):
    def __init__(self, weight, speed, regularPrice, color):
        self.weight = weight
        super().__init__(speed, regularPrice, color)

    def doublegetSalePrice(self):
        if self.weight > 2000:
            discount_value = (self.regularPrice * 10) /100
            return self.regularPrice - discount_value
        else:
            return self.regularPrice

class Ford(Car):
    def __init__(self, manu_discount, speed, regularPrice, color):
        self.manu_discount = manu_discount
        super().__init__(speed, regularPrice, color)

    def doublegetSalePrice(self):
        return self.regularPrice - self.manu_discount

class sedan(Car):
    def __init__(self, length, speed, regularPrice, color):
        self.length = length
        super().__init__(speed, regularPrice, color)

    def doublegetSalePrice(self):
        if self.length > 20:
            dis_value = (self.regularPrice * 5) / 100
            return self.regularPrice - dis_value
        else:
            dis_value = (self.regularPrice * 10) / 100
            return self.regularPrice - dis_value
truck = Truck(2050, 270, 130000, "black")
print("final price of truck = ", truck.doublegetSalePrice())
ford = Ford(500, 240, 1000000, "red")
print("final price of ford = ",  ford.doublegetSalePrice())
sedan = sedan(25, 250, 1200000, "black")
print("final price of sedan = ", sedan.doublegetSalePrice())
