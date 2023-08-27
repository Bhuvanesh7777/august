print("Write a python program to remove a given  character from string")
str = input("enter a string")
print ("Original string: " + str)
remove_str = str[:2] +  str[3:] 
print ("String after removal of character: " + remove_str)

print()
print()
print()


print('Write a program to check String is Palindrome or not')
string=input('enter a string')
if (string==string[::-1]):
   print('string is palindrome')
else:
   print("string is not a palindrome")  

print()
print()
print()

print('Write a python program to check given character is vowel or consonant')
character=input("enter a character:")
vowels=['a','e','i','o','u','A','E','I','O','U']
if character in vowels:
   print('character is vowel')
else:
   print('char is not a vowel')

print()
print()
print()

print('Write a python program to replace string space with given character in Python')   
string=input("enter a string")
character='.'
string=string.replace("",character)
print(string)

print()
print()
print()

print('Write a python program to count alphabets, digits, and special characters in the string')
string = input("Please Enter a String : ")
alphabets = 0
digits = 0
special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print(" Number of Alphabets in this String :  ", alphabets)
print(" Number of Digits in this String :  ", digits)
print("Number of Special Characters in this String :  ", special)

print()
print()
print()

print("Write a python program to remove all the blank spaces in a given string")
string = input('enter the string:')
str1= string.lstrip()
print(str1)          

print()
print()
print()


print("Write a python program to find sum of integers in the string")
str1 = input('Enter a string: ')
sum=0
for i in str1:
    if i.isdigit():
        sum=sum+int(i)
print("sum=",sum)

print()
print()
print()

print("Write a python program to Remove Repeated Character from String")
string=input("enter a string")
str1=""
for char in string:
    if char not in str1:
        str1=str1+char
print(str1)

print()
print()
print()

print("Write a python program to count occurrence of given character in string")
string=input("enter a string")
char=input("enter a char")
occurrence_character=string.count(char)
print(occurrence_character)

print()
print()
print()

print("Write a python program to check string is anagrams or not in Python")
str1=input("Enter string 1:")
str2=input("Enter string 2:")
count=0
for i in str1:
    for j in str2:
        if i==j:
            count=count+1
if count==len(str1):
    print("Strings are anagram of each other")
else:
    print("Strings are not anagram of each other")