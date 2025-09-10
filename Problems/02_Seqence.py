'''
Input : tup=(1,5,9,13,17)
Output : 1,5,9,13,17,21,25,29
Explanation: it's an increasing sequence by 4. So the next three numbers ar 
17+4=21,...     
Also (3,-1,-3,-5)'''

def sequence(tup):

    if len(tup)<2:
        return tup
    diff=tup[1]-tup[0]
    numbers=tuple(tup[-1]+diff *i for i in range(1,4))
    return tup+numbers
tup=(1,5,9,13,17)
tup1=(3,-1,-3,-5)
print(sequence(tup))
print(sequence(tup1))