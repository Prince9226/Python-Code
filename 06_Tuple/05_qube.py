# write a program create user define tuple print number with qube:
n=int(input("How many number you want put in main tuple:"))
list=[ ]
i=1
while(i<=n):
    list2=int(input("Enter the number:"))
    c=(list2,list2**3)
    list.append(c)
    i+=1
user_tuple=tuple(list)
print(user_tuple)
