class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.model=model
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("acelerating...")
        "acelerator functionality here"

    def change_gear(self,gear_type):
        print("Gear Changed")
        "gear related functionality here"

tesla = Car("modelY","blue","Tesla","120")
print(tesla.start())
print(tesla.color)