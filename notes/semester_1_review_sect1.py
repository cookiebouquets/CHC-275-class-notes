"""
    Review of Semester 1
"""

#Question: How do we print to the terminal print()
#2nd Question: What goes inside the parentheses for print()
#A: the message

print("hello world")

"""
    Variables: What are associated with variables
        1) their name
        2) Their data type
        3) the data itself
        
    Data types: Strings (plaintext), integers (ints: whole numbers), floating point numbers (floats)
    True or False (booleans)
    
    How do we make a variable?
    
    name = data
"""


var2 = "hello world" 

#how do we print var1?




"""
    Accepting keyboard input:
    
    How do we make the terminal ask for input? 
    There is a function  that stops the program and waits until the user types something in
    
    input()
    
    input() stops the program and waits for a user input 
    
    qualities of input()
    
    1. Does input() accept an argument? 
    Yes - what goes inside input()'s parentheses
    string - what does this string represent 
    
    input() does two things, stops the program, prints its argument, and then waits for keyboard input
    
    what do we call the string that input prints: prompt
    
    input(prompt) -> stops control of the program -> prints prompt -> waits for keyboard input
"""
#we want the user to put a number into var1
#var1 = input("input a number 1-10")
#print(var1)


"""
    Typecasting:
    
    Question: What is the return type for input() 
    
    Return type: The data associated with the value that is returned by the function
"""

def add(x,y):
    x = x + y
    print(x)
    #go back to main where add left off


"""
    i've made a function called add. 
    
    Line 68 is called a function header. 
    
    Function headers have 3 parts to it
        - def keyword: It stops the program and tells the computer to create a function
        - function name: the name of the function
        - parameter list: things in the parentheses for the function to use
        
    in our add example:
        - def keyword: we have it
        - function name: add
        - parameter list: x and y
        
    what does return do? 
        - we talked about scope.
        - global scope: stuff inside def main():
            we say a variable has global scope if it is defined in def main 
            when we call a function that has parameters
            those parameters now have local scope 
            
            So in the add example, there are two x's
            
            x in main
            x in add()
            
            x:main =/= x:add
            
            so things in local scope do not affect things in global scope 
            
            overall: variables do not leave their scope. 
"""

""" 
def main():
    x = 5
    #when i call the add function 
    #main function "always in control"

        We say a function is in control when the body of the function is running  

    add(x,6) #the main function will suspend its control and pass it to the add function
    #this is called passing control. In this case it will go to line 69
    print(x)
"""    


"""
    question: What is going to happen when I run this? 
    
    question: What happens during a function call
"""


"""
    So why did we talk about scope? it's because we want to get the result of a function out of its scope
    When a function call is over it will destroy everything in local scope
"""

def example():
    var1 = "hello"
    return var1 #what return does is show the thing after return to main 
    

def main():
    result = example()
    #question will i be able to print var1 in main?
    #print(var1)
    #python does automatic memory allocation. So when a function is done, it will destroy
    #everything in its scope 
    print(result)
    
#main()
    
    
"""
    How do we save var1? 
    
    That is the whole purpose of the return keyword 
    What return does is flag the computer to save the thing after the return keyword 
    The thing is, you now have to save that result into a variable in the scope outside of it 
"""


"""
    What is the return type of input()?
    
    How do we check this? 
"""

#input()

"""
input return type = string.

practically that means every time we type in input() we're gonna get a string, even if we type in a number


"""
#num= int(input("type ina number "))
#print(5 + num)




"""
    we fix this by typecasting
    
    int() float() str()
    
"""

"""
    that's everything we have for variables and input() (and also functions kind of)
    
    Control structures: 
        -sequence: evaluate code line by line one after another
        -selection: a choice has to be made EITHER OR
        -iteration: repeat a block of code until a condition is met 
"""

print(1)
print(2)
print(3)

#sequence corresponds to line by line execution

"""
    if-elif-else logic:
    
    syntax for this
    
    if <condition>:
    
    condition has to be something that can be evaluated to true or false
    
    examples of conditions
    
    5 ==5: True
    4 == 5: False
    not 4 ==5: True 
"""
"""
choice = int(input("enter your number: "))

if choice ==5:
    print("our number is equal to 5")
else:
    print("your number is not equal to 5")
"""

"""
    we say the thing after the "if" keyword is called the conditional.
    
    Question: 
    
    Do we know the difference between
    
    if
    if
    if
    
    if
    elif
    elif 
    
    
"""

"""
num = int(input("enter num "))

if num % 2 == 0:
    print("your number is divisible by 2")
elif num % 5 == 0:
    print("your number is divisible by 5")
"""

    
"""
    think of if as a function and the thing underneath being the body. After "if" is done, it will jump
    past ALL ELIFS AND ELSES
    
"""
"""
    num = int(input("enter num "))
if num % 2 == 0:
    print("your number is divisible by 2")
if num % 5 == 0:
    print("your number is divisible by 5")
"""

    
    
"""
    How do we repeat a line of code? 
    
    -while loop
    -for loop 
    
    while loop first
    
    syntax for while loop is
    
    while <conditional>: 
"""

num = 1
while num < 5:
    print(num)
    num = num + 1
    
"""
    So what we need for while loops, is GUARANTEE that the while loop will end we did this by incerementing
    num by 1 until num = 4
"""

check = True
while check:
    option = input("would you like to exit?")
    if option == "y":
        check = False
        
        
"""
    basic menu structure is dependent on a check variable and if statements
"""

"""
    lists
    
    how do we make an empty list?
"""

mylist = []

"""
    square brackets for lists. 
    
    lists store multiple variables at addresses called "indices" or "index" (singular)
    what are the possible values for our indices
    
    0,...,len(list)-1
    
    its len(list) -1 because 
    
    0,....,len(list) is a list of len(list)+1 variables
"""
mylist = ["hi","orange","chc"]

"""
    how do we access lists at a particular index?
    
    square brackets
    
    list[index]
"""

print(mylist[1])

