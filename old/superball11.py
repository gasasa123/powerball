import random
w = [random.randrange(1, 20, 1) for i in range(5)]
g = [random.randrange(1, 10, 1) for i in range(1)]
winner = (w,g)
print("The winner number is :", winner)
white = [random.randrange(1, 20, 1) for i in range(5)]
gold = [random.randrange(1, 10, 1) for i in range(1)]
my_number = [white,gold]
print("My number is : ",my_number)

counter = 0
for i in w:
    for y in white:
        if i == y:
            counter += 1
print("you have" + str(counter), "white balls")
counter1 = 0
for i in g:
    for y in gold:
        if i == y:
            counter1 += 1
print("gold ball :", counter1)
if counter == 5 and counter1 == 1:
    print("you wan : 324,000,000 $ ")
elif counter == 5 and counter1 != 1:
    print("you wan : 1,000,000 $ ")
elif counter == 4 and counter1 == 1:
    print("you wan : 10,000 $ ")
elif counter == 4 and counter1 != 1:
    print("you wan : 100 $ ")
elif counter == 3 and counter1 == 1:
    print("you wan : 100 $ ")
elif counter == 3 and counter1 != 1:
    print("you wan : 7 $ ")
elif counter == 2 and counter1 == 1:
    print("you wan : 7 $ ")
elif counter == 1 and counter1 == 1:
    print("you wan : 4 $ ")
elif counter == 0 and counter1 == 1:
    print("you wan : 4 $ ")
else:
    print("Try again !! ")