#Loops
colors = ['blue', 'yellow', 'pink', 'red']
for color in colors:
    print(color)


colors = ['blue', 'yellow', 'pink', 'red']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'pink':
        break
    print(color)

#Tuples loop
point = (1.2, 2.1, 4.0)
for value in points:
    print(value)

#Dictionary loop
ages = { 'Alan':20, 'Pedro':19, 'Juan':15}
for key in value:
    print(f"{key} is {value} years old")

#String loop
for letter in "my_string":
    print(letter)

#Unpacking Items with a loop
list_of_points = [(1,2), (6,7), (8,9), (3,5)]
for x,y in list_of_points:
    print(f"x: {x} | y: {y}")

for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")

