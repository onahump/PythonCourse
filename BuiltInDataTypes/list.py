my_list = [1, 2, 3, 4, 5]
my_list
my_list[0]
my_list[4]
my_list[7]
length = len(my_list)
length = len("Hello")
split = my_list[0:2]
split2 = my_list[2:4]
splituntilfour = [:4] # This'll wive us until the number 4
splitpairs = my_list[::2]  # This'll substract pair numbers  = [1,3,5]
reverselist = my_list[::-1] # This'll reverse the numbers = [5,4,3,2,1]
my_list[0] = 'a' # Assingning value in 0 index
my_list[0:2] = 'a' # This'll return ['a', 3, 4, 5] because this is getting both indexes 0 & 1
my_list[0:2] = [1,2,3] # This'll put the numbers inside the list
my_list[0:2] = [] # Removing values
my_list.append(6)
my_list.remove(4)
my_list.pop() # This'll return the last value & it'll remove this value
my_list.insert(1,3) # var.insert(index , numbert to insert)


