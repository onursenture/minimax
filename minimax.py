# artificial intelligence homework 3 - fall 2011 bilkent university
# minimax demonstration
# author: onur senture http://github.com/onursenture
#  -*- coding: utf-8 -*-

def game():
    
    level3 = [0, 0, 0, 0, 0, 0, 0, 0]
    level2 = [0, 0, 0, 0]
    level1 = [0, 0]
    level0 = [0]

    allDone = False
    allNodes = [line.strip() for line in open("inputs.txt")]

    while allDone != True:

        points = 0
        i = 0

        # level 3
        while points != 16:
            if allNodes[points] < allNodes[points + 1]:
                level3[i] = allNodes[points]
            else:
                level3[i] = allNodes[points + 1]
            i = i + 1
            points = points + 2
        print "level 3: ", level3

        points = 0
        i = 0

        # level 2
        while points != 8:
            if level3[points] > level3[points + 1]:
                level2[i] = level3[points]
            else:
                level2[i] = level3[points + 1]
            i = i + 1
            points = points + 2
        print "level 2: ", level2

        points = 0
        i = 0

        # level 1
        while points != 4:
            if level2[points] < level2[points + 1]:
                level1[i] = level2[points]
            else:
                level1[i] = level2[points + 1]
            i = i + 1
            points = points + 2
        print "level 1: ", level1

        points = 0
        i = 0

        # level 0
        while points != 2:
            if level1[points] > level1[points + 1]:
                level0[i] = level1[points]
            else:
                level0[i] = level1[points + 1]
            i = i + 1
            points = points + 2
        print "level 0: ", level0
 
        allDone = True

if __name__ == "__main__":
    game()