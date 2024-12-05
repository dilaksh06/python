class car ():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"{self.make},{self.model},{self.year}")
    def start_engine(self):
        print("The engine of the car is now running.")
    def stop_engine(self):
        print("The engine of the car is now off.")


class ElectricCar(car):
     def __init__(self,make,model,year):
         super().__init__(make, model, year)
     def charge(self,battery_size):
        self.battery_size=battery_size
        print(f"Charging the electric car with a {self.battery_size} kWh battery.")
    
        
        
    
car1 = car("Toyota", "Corolla", 2020)
car1.display_info()
car2=car("Toyota", "Corolla", 2020)
car2.stop_engine()
car2.start_engine()
car3=ElectricCar("Toyota", "Corolla", 2020)
car3.charge(50)
