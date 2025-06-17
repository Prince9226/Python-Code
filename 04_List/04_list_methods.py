l1=[2,4,5.3,"Prince","yadav",2,2,6.32,]
l1.append(23)  ## Adds an element at the end of List.
print(l1)

print(l1.copy())     ## Returns a copy of the list.


print(l1.count(2))    ## Returns the number of elements with the specified value.


city=["Ghazipur","london","Gurogaon"]
l1.extend(city)     ## Adds the elements of a list (or any iterable) ,to the end of current list.
print(l1)

print(l1.index("Prince"))   ## Returns the index of the first element with the specified value.


l1.insert(2,"anish")   ## Adds an element at the specified position
print(l1)

print(l1.pop(1))   ## remove the element at the specified position.


l1.remove(2)       ## remove the first item with the specified value.
print(l1)

l1.reverse()    ## reverse the order of the list.
print(l1)

l2=[2,5,7,4,1,6]
l2.sort()   ## sort the list
print(l2)

l1.clear()     ## removes all the elements from the list.
print(l1)

