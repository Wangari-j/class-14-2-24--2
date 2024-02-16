class Car:
    name = ""
    model = ""

    def __init__(self,name,model,):
      self.name = name 
      self.model = model



car1 = Car("subaru","impreza")

print(car1.model)

car2 = Car("toyota", "land cruiser")
car3 = Car("nissan", "note")

print(car2.name, car3.name)
print("is the biggest car brand in Kenya.")



