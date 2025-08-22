# write a program user define dict.
dict={}
n=int(input("Enter the number:"))
i=1
while(i<=n):
    key=input("Enter the key")
    data=input("Enter the data")
    dict[key]=data
    i+=1
    print(dict)
