import random
import colorama
def winnerlist (a,b,c,d):
    winner = []
    a = [random.randrange(1, 20, 1) for i in range(5)]
    b = [random.randrange(1, 10, 1) for i in range(1)]
    winner.append(a+b)
    sorted_numbers = sorted(winner)
    print("The winner number is :", sorted_numbers)
    my_number = []
    c = [random.randrange(1, 20, 1) for i in range(5)]
    d = [random.randrange(1, 10, 1) for i in range(1)]
    my_number.append(c+d)
    sort_num = sorted(my_number)
    print("My number is : ", my_number)

    counter = 0
    for i in a:
        for y in c:
            if i == y:
                counter += 1
    print("you have" ,counter, "white balls")
    counter1 = 0
    for i in b:
        for y in d:
            if i == y:
                counter1 += 1
    print("gold ball :", counter1)
    if counter == 5 and counter1 == 1:
        print("you wan :  Jackpot 324,000,000 $ ")
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