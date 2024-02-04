# Define a base class called Adult.
class Adult:
    # Constructor to initialize attributes.
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name 
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
    
    # Method to determine if an adult can drive.    
    def car_drive(self):
            print(f"{name} is old enough to drive.")

# Define a subclass called Child.               
class Child(Adult):
    # Method to override the car_drive method.
    def car_drive(self):
        print(f"{name} is too young to drive.")

# Get input from the user.      
name = input("What is your name? ")
age = int(input("How old are you? "))
hair_colour = input("What is the colour of your hair? ")
eye_colour = input("What is the colour of your eyes? ")

# Check if the age indicates whether the person is old enough to drive or not.
if age >= 18:
    adult = Adult(name, age, hair_colour, eye_colour)
    adult.car_drive()
else:
    child = Child(name, age, hair_colour, eye_colour)
    child.car_drive()

