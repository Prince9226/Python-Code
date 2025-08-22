d1={}
n=int(input("Enter the number:"))
for i in range(1,n+1):
    key=input("Enter the key values:")
    data=input("Enter the data values:")
    d1[key]=data
print(d1)
x=d1.values()
for i in x:
    print(i)
y=d1.keys()
for i in y:
    print(i)
print(d1.pop(input("Enter the key value delete:")))  ## take key from user & delete that item.
print(d1)
for x,y in d1.items():
    #print(x)  #or   print(y)
    print(x,y)
for x in d1:
    print(x)
x=d1.keys()
print(type(x))
x=d1.keys()
print(sorted(x))
