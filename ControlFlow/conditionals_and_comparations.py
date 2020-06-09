#Comparasions
1 < 2 # 1  Less than 2? This will return false
2 > 1 # 2 greather than 1? This will return true
2 == 2 # 2 is equal to 2 ?
1 != 3 # 1 is different to 3
100 <= 2 # less or equal
100 >= 1 # greather or equal
1.1 == "1.1" #False - Different type
1.1 == float("1.1") # Same type
"this" == "this" #True
"This" == "this" #False
"b" > "a" #True
"abc" < "b" #True

# The in Check
2 in [1, 2, 3, 4] #True
4 not in [1, 2, 3, 5] #True

#If
if False:
    print("Was True")

#If / Else
if False:
    print("Was True")
else:
    print("Was False")

#Else if
name = "Kevin"
if len(name) >= 6:
    print("name is long")
elif len(name) == 5:
    print("name is 5 characters")
elif len(name) >= 4:
    print("name is 4 or more")
else:
    print("name is short")

