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
weight = int(input("entet the wieght of the truck= "))
speed = int(input("enter the speed of the truck= "))
price = int(input("enter the price of the truck= "))
color = input("enter the color of the truck= ")
truck = Truck(weight, speed, price, color)
print("final price of truck = ", truck.doublegetSalePrice())
manufacture_discount = int(input("entet the manufacture discount  of the ford= "))
speed =	int(input("enter the speed of the ford = "))
price =	int(input("enter the price of the ford= "))
color =	input("enter the color of the ford= ")

ford = Ford(manufacture_discount, speed, price, color)
print("final price of ford = ",  ford.doublegetSalePrice())
length = int(input("entet the length of the sedan = "))
speed =	int(input("enter the speed of the sedan = "))
price =	int(input("enter the price of the sedan = "))
color =	input("enter the color of the sedan = ")

sedan = sedan(length, speed, price, color)
print("final price of sedan = ", sedan.doublegetSalePrice())
