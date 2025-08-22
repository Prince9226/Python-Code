##finding 2 given range 
a=int(input("Enter the number:"))  
b=int(input("Enter the number:"))
c=[x for x in range (a,b) if '2'in str (x)]
print(c)
