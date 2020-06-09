#Tuples

point = (2.0, 1.0) # This is a tuple (x , y)
point[0] = 1 # ERROR: Tuples can't be modified
point_3d = point + (4.0, ) # (x, y , z)
print(point_3d)
x, y , z = point_3d #This'll assign the value of the tuple into the variables x, y & z
print(x) # 2.0
print(y) # 1.0
print(z) # 4.0
print("My name is %s %s" % ("Name", "LastName"))

#Ranges

range(10) # range(0, 10)
list(range(0, 10)) #[0,1,2,3,4,5,6,7,8,9]
list(range(0, 12, 2)) # Initial range, Final Range, Step = [1,3,5,7,9,11]



