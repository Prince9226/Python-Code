'''
Input: n=10 , arr[]=9,8,7,4,4,2,1,1,9,8  , x=1
output: 1,2,4,7,8
erased 1
3,4,7,8,9'''

def setInsert(s,n):
    s=set()
    for i in range(n):
        s.add(arr[i])
    return s

def display(s):
    for val in sorted(s):
        print(val,end=" ")
    print()


def setErase(s,x):
    if x in s:
        s.remove(x)
        print("erased" ,x)
    else:
        print("Not found")

n = 10
arr = [9, 8, 7, 4, 4, 2, 1, 1, 9, 8]
x = 1

s = setInsert(arr, n)   # Insert elements into set
display(s)              # Display set

setErase(s, x)          # Erase element x

display(s) 
