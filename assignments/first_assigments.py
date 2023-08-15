creating table using For and While loop
num=int(input('Enter a number :'))
for i in range(1,11):
    print(num,' x ',i,' = ',num*i)

num=int(input("enter a number:"))  
counter=1
while counter<=10:
    print(num,' x ',counter,'=',num*counter)
    counter+=1 


creating a logic using conditional statements
score=80
if score >=90:
    grade='a'
elif score >=70:
   grade='b'
elif score >=50:
    grade='c'
else:
    grade='f'
print("your grade is:", grade) 


creating a logic using logical and realtional operators

passing_score=60
science_score= int(input('enter your science score:'))
math_score=int(input('enter your math score:'))
if math_score>=passing_score and science_score>=passing_score:
    print('pass')
else:
    print('fail')
       


