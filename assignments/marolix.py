#programm to get square of every element by using map fucntion
#numbers=eval(input("Enter a list"))
#l= map (lambda n: n*n, numbers)
#print(list(l))

#program to convert a list of integers to string representation
#numbers=eval(input("enter a list:"))
#l= list(map(lambda n: str(n), numbers))
#print(l)

#program to calculate the length of words in a list of strings
#words=["apple","Mango","Cherry"]
#l=list(map(lambda n: len(n), words))
#print(l)







#from functools import*
#program to product all the elements in a list
#l=eval(input('enter a elements: '))
#product =reduce(lambda a,b : a*b,l)
#print(product)

#program to find the maximum values in the list
#numbers=eval(input("enter the elements:"))
#max_value=reduce(lambda a,b : a if a>b else b , numbers)
#print(max_value)

#program to find sum of digits in the list
#numbers=eval(input("Enter a elements:"))
#sum=reduce(lambda a,b: a+b, numbers)
#print(sum)





#nested function to get numbers multiplied by 3and divided by 3 of given number
#def mul(x,y):
#    print(f'multiplied by 3 = {x*3,y*3}')
#    def div(x,y):
#        print(f'divided by 3 = {x/3,y/3}')
#   div(x,y)
#x=int(input('enter a number 1: '))
#y=int(input('enter a number 2: '))
#mul(x,y)

#nested function to get sum and product of given numbers
def sum(x,y):
    print(f'sum = {x+y}')
    def pro(x,y):
        print(f'pro = {x*y}')
    pro(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
sum(x,y)


