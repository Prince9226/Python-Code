num=int(input("Enter the number for Reverse Half Pyramid Patter(Left-Sided):"))
for i in range(num,0,-1):
    for j in range(num-i+1):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()



## Output
'''
Enter the number for Reverse Half Pyramid Patter(Left-Sided):5
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
          '''
