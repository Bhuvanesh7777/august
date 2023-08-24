print('Membership operator using in')
string='Bhuvanesh'
if 'n' in string:
    print('valid')
else:
    print('not valid')

print('Membership operator using not in')
if 'n' not in string:
    print('valid')
else:
    print('invalid')

print()
print()
print()    


print('Removing spaces from string')
s=" marolix technology solutions  "
print(len(s))
after_strip=s.strip()
after_strip=s.rstrip()
after_strip=s.lstrip()
print(len(after_strip))
print(after_strip)

print()
print()
print()

print("Comparing of two strings")
s1=input("Enter a s1:")
s2=input("Enter a s2:")
if s1==s2:
 print("Both are same")
else:
 print("Both are not same")

 print()
 print()
 print()

print('Finding substrings by using index method')
s='marolix technology solutions'
sub_string='o'
s1=s.index(sub_string)
print('index position of given sub_string is s1')

print()
print()
print()

print('Finding substrings by using rindex method')
s='marolix technology solutions'
sub_string='o'
s1=s.rindex(sub_string)
print('rindex position of given sub_string is s1')

print()
print()
print()


print("Finding substrings by using find method")
s='marolix technology solutions'
sub_string='o'
s1=s.find(sub_string)
print('index position of given sub_string is s1')

print()
print()
print()


print('Finding substrings by using rfind method')
s='marolix technology solutions'
sub_string='o'
s1=s.rfind(sub_string)
print('index position of given sub_string is s1')

print()
print()
print()


print('replace the string using replace method')
string='kakinada is good city'
s1=string.replace('good', 'bad')
print('replaced string: {s1}')

print()
print()
print()


print('Separate the string using split method')
s='kakinada is good city'
print(len(s))
s1=string.split()
print('separated string: s1')

print()
print()
print()


print('Join the strings using join method')
list=['kakinada', 'is', 'good', 'city']
print(len(list))
s1=(':').join(list)
print('New string after joining: s1')