bool("") #false

#NOT operation
not("") #true Opposite
not 1 > 2 #true
if not 1 > 2
    print("no it isn't")

#OR Value - The or operation will return the first value that is "truthy" or the last value in the chain:
last = ""
last_name = last or "Doe"
last_name # This will return Doe

#AND Value - which requires both conditions to be True
first = "Keith"
last = "Thompson"
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}") #Full name: Keith Thompson

