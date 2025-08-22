n=int(input("Enter the elements:"))
elements=[]     ###  user define tuple by type casting.
i=1
while(i<=n):
    element=input("Enter the no.:")
    elements.append(element)
    i = i+1
user_tuple=tuple(elements)
print(user_tuple)
