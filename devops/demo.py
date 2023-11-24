# welcome, in this simplest project, you will run your very first python command!
# this file contents many different ( small ) python script, to use them you have to remove the multi-line-comment (''' at the beginning and the end of each )

# simple addition in python
'''y = 70
x = 130 
t = 1000
tt = (y + x + t)
print(tt)'''


# how to use a function in python
'''def demo_function():
    print('hello you are about to get hired by a very big IT company')

demo_function()'''


# how to use input in python
'''email = input("please enter your email address: ")
print('your email address is:' , email)'''



# how to use int in python 
# so that you can add 2 things togheter
'''a = int(input(' Enter value of a '))
b = int(input(' Enter value of b '))
c = a + b

print (c)'''



# is keywords in python

'''r = 10 
w = 18
e = 199
print(r is e)'''



# relational operators in python
'''d = 12
f = 3 
print(d == f)'''



# if, elif, else conditions in python
'''x = 25000
if x > 10000:
    print("life is good, I will be very rich")

elif x == 150000:
    print("if I study very hard, I can be happy one day")

elif x < 10000:
    print("I need to do some business,poverty is very bad")

else: 
    print("have fun, boy")'''




# for loop in python, always start with for
# it is the best way to run a repetitive task until the conditions are met

    # print(i, "good morning Engineer"), will show all the different line in your code

'''for i in range(10):
    print("good morning Engineer")
print("congratulation on your new position")'''



# while loop in python, always start with while
# it only stop when the condition is met

'''password = None
while password != "admin123@":
    password = input("Enter your password ")
    if password != "admin123@":
        print("incorrect password, try again ")
print("you have login successfully ")'''



# infinite loop, it never end, usually use for video game or ...
# please note that you will have to stop by pressing ctr + c on windows
# overwise it won't stop and can cause your cpu problem 

'''while True:
    print("sorry, please try again ")

while 25 > 15:
    print("sorry, please try again")

while "Hello" == "Hello":
    print("sorry, please try again")'''



# break and continue statement in python
# it causes the code to break and exit the loop
# in this simple example, it will break when the loop 7


'''for i in range(20):
    print(i)
    if i == 7:
        break
print("loop exited")'''


# break with wile loop in python
# in this simple example, it will stop only when you type the letter q

'''while True:
    out = input("type q to exit the loop ")
    if out == 'q':
        break
print("loop exited")'''


# the continue statement
# here, it will skip 3 and continue the for loop

for i in range(7):
    if i == 3:
        continue
    print(i)

