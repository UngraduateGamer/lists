# list is created by the [] and separated with commas,
lists=['name','rohan','ram','misti','suman']
print(lists)
print(lists[0:-1:2])

print(lists[0]) # print only first index 

# list methods
l=[11,55,45,85,1,52,1,2,44,1,5,3,5,1,5]

l.sort() # sort() function used to arranging the elements in the AScendng order
print(l)

l.sort(reverse=True) # sort(reverse=True) function used to arranging the elements in the REversing order
print(l)

l.append(5) # add 5 in the last of the list
print(l)
l.count(1)
l.insert(1,58) # add 1 index in the 58 elements
