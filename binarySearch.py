import math
ramList=[2,10,15,17,21,28,40,55,60,61,62,83]

#posLu = upper limit position
#posLo = lower limit position
#posMid = mid position

def binSearch(values,searched):
    posLo = 0
    posLu = len(ramList)-1
    while(posLu<=posLu):
        posMid=math.ceil((posLo+posLu)/2)
        hint = values[posMid]
        if(hint == searched):
            return posMid
        if(hint>searched):
            posLu= posMid-1
        else:
            posLo=posMid+1
    return -1

print(binSearch(ramList,60))