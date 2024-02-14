class car:
    name = ""
    model = ""

def __init__(self,name,model,):
    self.name = name 
    self.model = model



car1 = car
car1.name = "Subaru"
car1.model = "Impreza"

print(car1.model, car1.name)

car2 = car()
car3 = car()

car2.name = "Toyota"
car2.model = "Land cruiser"
car3.name = "Nissan"
car3.model = "Note"

print(car2.model, car3.model)
print(car2.name + " is the biggest car brand in Kenya.")



