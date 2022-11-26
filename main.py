# write your code here
my_name = input()
my_age = input()
print(f'My name is {my_name} and I am {my_age} years old')

first_number = 5
second_number = 8
operation = input()
if '+' in operation :
    print(first_number+second_number)
elif '-' in operation :
    print(first_number-second_number)    
elif '*' in operation :
    print(first_number*second_number)
elif '/' in operation :
    print(first_number/second_number)    
else :
    print('the operation is not valid')    

x = eval(input())
noun = input("plural")
name = input('your name')    
statment = input('write your statment')
verb = input('write any verb')
print(f'It was {x} oclock when I heard a knock at the door.I opened the door and there was a box full of {noun} with a note saying {name} , {statment} and I {verb} .')