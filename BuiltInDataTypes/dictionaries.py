ages = {'Kevin': 29, 'Pedro': 29, 'Pablo': 15} # Creating a dictionary
ages['Nahum'] = 10 #Adding a value
del ages['Kevin'] #Deleting a value, also we can delete accdidentally the varable using del
ages.pop('Pedro') #Substracting a value
ages.get('Pablo') #This will return the actual value
ages.keys() # dict_keys(['Pedro', 'Pablo'])
list(ages.keys()) # ['Pedro', 'Pablo']
ages.values()
list(ages.values())

#Alternative
weights = dict(pancho=20, manuel=12, carlos=21)
print(weights) # {'pancho': 20,'manuel': 12, 'carlos': 21}

#Also you can pass a tuple
colors = dict([('lalo', 'yellow'), ('Roberto', 'blue')])
print(colors) # {'lalo': 'yellow', 'Roberto': ''blue}




