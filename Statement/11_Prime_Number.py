n=int(input("Enter the number:"))
count=0
i=1
while(i<=n):
    if(n%i==0):
        count=count+1
    i+=1
if(count==2):
    print(n,"is prime")
else:
    print(n,"is not prime")
