class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("BMW", "M4")

car1.display_info()
car2.display_info()