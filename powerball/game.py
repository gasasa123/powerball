import random
class Lists:

    def mynumbers(self):
        my_number = []
        c = [random.randrange(1, 21) for i in range(5)]
        d = random.randrange(1, 11)
        my_number.append(c)
        my_number.append(d)
        # sorted_number = sorted(my_number)
        return my_number
