## WAP to create two different list of the same number of elements and print the sum of their curesponding elements.
l1=[2,4,3,5]    
l2=[3,1,3,8]      
sum_list=[]
for i in range(len(l1)):
    sum_list.append(l1[i] +l2[i])
print(sum_list)
