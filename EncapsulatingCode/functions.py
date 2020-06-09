def hello_world():
    print("Hello world!")

hello_world()

def print_name(name):
    print(f"Hello {name}")

print_name("Juan")
output = print_name("Pancho") #Assigning function result into a variable

def add_two(num): #Adding two
    return num + 2

result = add_two(2)
print(result)

#Multiple arguments
def add(num1, num2):
    return num1 + num2
result = add(3,5)
print(result)

#keyword Argumment
def contact_card(name, age, car_model):
    print(f"{name} is {age} years old and drives a {car_model}")

def contact_card("Alan", 30, "Hyundai")

def contact_card(name="Pedro", age=21, car_model="Bugatti") #Keyword Arguments
def contact_card(car_model="Ferrari", name="Alvaro", age="28") #Keyword Arguments, no matter the order

def contact_card((car_model="Ferrari", "Alvaro", age="28") #ERROR: Missing name argument

#Defining Default Arguments
def can_drive(age, driver_age=18):
    return age >= driver_age
can_drive(16)
can_drive(21)
