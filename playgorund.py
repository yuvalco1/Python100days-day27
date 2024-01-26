def add (*args): # *args is a tuple , could be multiple arguments
    print (args[0])
    sum = 0
    for n in args: # loop through tuple
        sum += n
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))


def calculate(**kwargs):
    print(kwargs) # **kwargs is a dictionary with key value pairs
    for key, value in kwargs.items(): # loop through dictionary
        print(key)
        print(value)
    print(kwargs["add"]) # access value by key
    print(kwargs["multiply"])

calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # get value by key
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)

