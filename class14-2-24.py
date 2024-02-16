#create class
class Colours:
    briColours = " "
    dullColours = " "
#the above are the attributes of the class 'colour'

#create objects of the class
Colours1 = Colours

#access my class attributes via my oject
Colours1.briColours = "white", "beige"
Colours1.dullColours = "Brown", "Black"

print(Colours1.briColours, Colours1.dullColours)

#I can create many objects of my  class
Colours2 = Colours()
Colours3 = Colours()
colours4 = Colours()

Colours2.dullColours = "navy blue"
colours4.briColours = "yellow"

print(colours4.briColours, Colours2.dullColours)
