class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        self.speed += m * 10
        return self.speed

    def brake(self, n):
        self.speed = max(0, self.speed - n * 10)
        return self.speed

class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=0):
        super().__init__(brand, speed)
        self.battery = battery

    def charge(self):
        self.battery = min(100, self.battery + 20)
        return self.battery

# 测试代码
if __name__ == "__main__":
    car = Car("Tesla")
    car.accelerate(3)
    print(f"加速后速度: {car.speed}")  # 输出: 30
    car.brake(2)
    print(f"刹车后速度: {car.speed}")  # 输出: 10

    e_car = ElectricCar("蔚来", 20, 60)
    e_car.accelerate(2)
    print(f"电动车加速后速度: {e_car.speed}")  # 输出: 40
    e_car.charge()
    print(f"充电后电量: {e_car.battery}")  # 输出: 80