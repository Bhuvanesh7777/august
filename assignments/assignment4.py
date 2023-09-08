#python program to merge two lists
#list1=list(eval(input('enter a number of elements')))
#list2=list(eval(input('enter a numberof elements')))
#list3=list1+list2
#print(f'Merging of two lists: {list3}')

#program to find the sum of list elements
#mylist=list(eval(input("enter number of elements")))
#print ("SUM:",sum(mylist))

#program to print even and odd numbers seperatly in list
#l=list(eval(input("Enter the elements:")))
#even=[]
#odd=[]
#for i in l:
# if i%2==0:
#    even.append(i)
 #elif i%2!=0:
 #   print("odd number")
 #   odd.append(i)
#print("even:",{even}) 
#print("odd:",{odd})  

#program to delete element of given index in list
#l=list(eval(input("Enter the elemnts")))
#index=int(input("enter the index position"))
#l.pop(index)
#print(l)

#program to delete given elemet from the list 
#l=list(eval(input("Enter the list:")))
#element=eval(input("Enter the element:"))
#l.remove(element)
#print(l)

#program to insert an elemet  at given index location
#l=list(eval(input("Enter the list:")))
#element=eval(input("Enter the element:"))
#index=int(input("Enter the index value:"))
#l.insert(element,index)
#print(l)

#program to check the sizes of given two lists are same
#l1=list(eval(input("Enter the first list:")))
#l2=list(eval(input("Enter the second list:")))
#if len(l1)==len(l2):
 #   print("sizes of given two lists are same:")
#else:
#    print("sizes of given two lists are same:")

#python function that takes two lists and returns True if they have at least one common member
#list1 = list(eval(input('enter the list1:')))
#list2 = list(eval(input('enter the list2:')))
#count=0
#for i in list1:
 #   for j in list2:
 #        if i==j:
#            count+=1
#if count > 0:
 #    print(True)
#else:
 #    print(False) 

# Python program to remove a specified column from a given nested list.
##Original Nested list:
#[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#After removing 1st column:
#[[2, 3], [4, 5], [1, 1]]

#l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#l1=[]
#for i in range(int(len(l))):
#    element=l[i]
 #   element.pop(0)
  #  l1.append(element)
#print(f'new list after removing specified elements: {l1}')

#program to convert a list of multiple integers into a single integer
#l = eval(input('enter the list:'))
#for i in l:
 #   print(i,end='')

#program to remove duplicates from a list
#l1=list(eval(input('enter a number of elements: ')))
#l2=list(set(l1))
#print(l2)