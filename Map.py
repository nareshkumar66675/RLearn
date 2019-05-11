import sys
import numpy as np
from Utils import *

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3


DefaultMap = [
        "S-------",
        "--------",
        "---x----",
        "-----x--",
        "---x----",
        "-xx---x-",
        "-x--x-x-",
        "---x---T"
    ]


class TreasureMap():


    def __init__(self, generate=True, customMap = None):

        if generate == True and customMap == None:
            desc = generate_random_map()
        elif customMap != None:
            desc = customMap
        else:
            desc=DefaultMap

        self.desc = desc = np.asarray(desc,dtype='c')
        self.nrow, self.ncol = nrow, ncol = desc.shape
        self.reward_range = (0, 1)

        self.nActions = 4
        self.nStates = nrow * ncol

        self.isd = np.array(desc == b'S').astype('float64').ravel()
        self.isd /= self.isd.sum()

        self.P = {s : {a : [] for a in range(self.nActions)} for s in range(self.nStates)}

        def to_s(row, col):
            return row*ncol + col

        def increment(row, col, a):
            if a == LEFT:
                col = max(col-1,0)
            elif a == DOWN:
                row = min(row+1,nrow-1)
            elif a == RIGHT:
                col = min(col+1,ncol-1)
            elif a == UP:
                row = max(row-1,0)
            return (row, col)

        for row in range(nrow):
            for col in range(ncol):
                s = to_s(row, col)
                for a in range(4):
                    li = self.P[s][a]
                    letter = desc[row, col]
                    if letter in b'Tx':
                        li.append((1.0, s, 0, True))
                    else:
                        newrow, newcol = increment(row, col, a)
                        newstate = to_s(newrow, newcol)
                        newletter = desc[newrow, newcol]
                        done = bytes(newletter) in b'Tx'
                        rew = float(newletter == b'T')
                        li.append((1.0, newstate, rew, done))



    def getMapText(self):
        row, col = self.s // self.ncol, self.s % self.ncol
        desc = self.desc.tolist()
        desc = [[c.decode('utf-8') for c in line] for line in desc]
        desc[row][col] = "(M)".format(desc[row][col])
        output = ''
        if self.lastaction is not None:
            output+="   Moving {}\n".format(["LEFT","DOWN","RIGHT","UP"][self.lastaction]) #print("Moving ({})\n".format(["Left","Down","Right","Up"][self.lastaction]))
        else:
            output+="\n" #print("\n")

        output+="\n".join('  '.join(line) for line in desc)+"\n"
        #print("\n".join('  '.join(line) for line in desc)+"\n")
        return output

    
    def clear(self):
        self.s = categorical_sample(self.isd, np.random)
        self.lastaction = None
        return self.s

    def PerformAction(self, a):
        transitions = self.P[self.s][a]
        i = categorical_sample([t[0] for t in transitions], np.random)
        p, s, r, d= transitions[i]
        self.s = s
        self.lastaction = a
        return (s, r, d, {"prob" : p})