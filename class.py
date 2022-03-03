class Car(object):
    def __init__(self,model,colour,company,speed_limit):
        self.colour=colour
        self.company=company
        self.speed_limit=speed_limit
        self.model=model

    def start(self):
        print("started")
    def stop(self):
        print("stoped")
    def accelerate(self):
        print("accelerating")
        "accelerator functionality here"
    def changeGear(self):
        print("gear changed")
        "gear related functionality here"
audi=Car("A6","red","audi",300)
print(audi.accelerate())                    