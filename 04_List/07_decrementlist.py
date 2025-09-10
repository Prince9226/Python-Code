''' You are given a list that contains integars.You need to decrement each element of the 
list by 1 and return the list'''

def decrementlist(arr):
    result=[]
    for i in arr:
        result.append(i-1)
    return result
arr=[]
n=int(input("How many number you want to list: "))
for i in range(0,n):
    b=int(input("Enter the number for list element :"))
    arr.append(b)
print(decrementlist(arr)) 