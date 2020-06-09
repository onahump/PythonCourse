while True:
    print("This'll never end")

count = 0
while count <=4: #While count is less than 4, this cicle will print "Looping message"
    print("Looping")
    count += 1

count = 1

#While count is less than 10 and it'll be divisible between 2 and residue is equals to 0 it'll contiue else this will print a message
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}") #Interpolation
    count += 1

count = 1
while count < 10:
    if count % 2 == 0:
        break   #This'll end the cycle
    print(f"We're counting odd numbers: {count}") #Interpolation
    count += 1







