class  Vehicle():
    def __init__(self, max_speed = 120, mileage = 100):
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return f"Vihecle with speed of {self.max_speed} and mileage of {self.mileage}"

car = Vehicle()
print(car)

# Child Class
class Benz(Vehicle):
    pass

benz = Benz()
print(benz)