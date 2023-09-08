#Write a Python script to add a key to a dictionary.
#d= { 0:10 , 1:20 }
#print(d)
#d.update({2:30})
#print(d)

#Python script to check whether a given key already exists in a dictionary
#d = {0:1,1:20,2:30,3:40,4:50,5:60}
#def key_is_present(x):
 #  if x in d:
 #     print("key is already exist")
  # else:
  #    print("key doesn't exist")
#key_is_present(5)
#key_is_present(7)   

#Python program to iterate over dictionaries using for loops
#d = {'Red': 1, 'Green': 2, 'Blue': 3} 
#for color_key, value in d.items():
 #    print(color_key, 'corresponds to ', d[color_key]) 

#Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys
#d={}
#for  i in range(1,16):
 #   d[i]=i**2
#print(d)  

#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string 
#str1 = 'marolix techonolgy' 
#my_dict = {}
#for letter in str1:
 #   my_dict[letter] = my_dict.get(letter, 0) + 1
#print(my_dict)

#python program to sum all the items in a dictionary
#my_dict={'data1':100,'data2':200, 'data3':300}
#print(sum(my_dict.values()))

#Python program to combine two dictionary by adding values for common keys
#from collections import Counter
#dict1 = {'a': 100, 'b': 200, 'c':300}  
#dict2 = {'a': 300, 'b': 200, 'd':400}  
#new_dict = Counter(dict1) + Counter(dict2)  
#print("The new  dict is:", new_dict)

#Python program to access dictionary key's element by index
#num = {'physics': 80, 'math': 90, 'chemistry': 86}
#print(list(num)[0])
#print(list(num)[1])
#print(list(num)[2])


#Python program to remove a key from a dictionary
#myDict = {'a':1,'b':2,'c':3,'d':4}
#print(myDict)
#if 'a' in myDict: 
 #   del myDict['a']
#print(myDict)

#Python script to merge two Python dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)