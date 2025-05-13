# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        print("Engine Started")

class Car():
    def __init__(self):
        self.engine = Engine()
    
    def engine_start(self):
        self.engine.start()

car = Car()
car.engine_start()