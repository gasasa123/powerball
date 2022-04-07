import random
from func import *
from game import Lists
class Game(Lists):

    def game(self):
        list1 = super().mynumbers()
        power1 = list1[-1]
        list2 = super().mynumbers()
        power2 = list2[-1]
        counter = 0
        flag = False
        for i in list1[0][0:5]:
            for y in list2[0][0:5]:
                if i == y:
                    counter += 1
        if power1 == power2:
            flag += True
        else:
            pass
        beauty(list1[0][0:5],power1)
        beauty1(list2[0][0:5],power2)
        resulte(counter,flag)




