''' Input = (3,5,6,7)
Output = 6,10,12,14
Explanation = multiplied numbers by 2'''
def doubleTup(numbers):
    return  tuple(x *2 for x in numbers)

Input=(2,3,4,5)
Output=doubleTup(Input)
print(Output)
       