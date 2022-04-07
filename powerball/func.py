
def resulte(counter, flag):
    if counter == 5 and flag == 1:
        print("you wan :  Jackpot 324,000,000 $ ")
    elif counter == 5 and flag != 1:
        print("you wan : 1,000,000 $ ")
    elif counter == 4 and flag == 1:
        print("you wan : 10,000 $ ")

    elif counter == 4 and flag != 1:
        print("you wan : 100 $ ")
    elif counter == 3 and flag == 1:
        print("you wan : 100 $ ")
    elif counter == 3 and flag != 1:
        print("you wan : 7 $ ")
    elif counter == 2 and flag == 1:
        print("you wan : 7 $ ")
    elif counter == 1 and flag == 1:
        print("you wan : 4 $ ")
    elif counter == 0 and flag == 1:
        print("you wan : 4 $ ")
    else:
        print("Try again !! ")

def beauty(x,y):
    print(f"your lucky numbers:\n{x},{y}",sep="-")

def beauty1(x,y):
    print(f"Today lucky numbers:\n{x},{y}",sep="-")