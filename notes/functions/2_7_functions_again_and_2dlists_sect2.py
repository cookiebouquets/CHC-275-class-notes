""" 
    Today we are going to finish up our conceptual understanding of functions and discuss multi-dimensional lists.
    
    
        IMPORTANT: Lab 6 Release will be Feb 14, Day 2
        IMPORTANT 2: If you have an extension on Lab 5 keep working on that 
    
        1. Painstaking Review of Functions again
        2. Review of Mutability
        3. Pass by Value vs Pass by Reference
        4. functions philosophically example 
        
        5. 2D lists 
        6. Iterating over 2D lists 
"""

#lets just start with making an example function and identify all of the parts of it 

def example(x1,x2): #<= Function Header, what is the parentheses? Parameters
    #Recall function signature: it's ordered tuple consisting of the return type and datatypes of parameters
    #x1,x2 are going to be integers and return is going to be an int: (int,int,int)
    #What is everything under the function header called? Function Body
    pass

def example2(h,y):
    """
    This is an example function
    parameter list:
        x1 <integer>: useful parameter for numbers
        x2 <integer>: not so useful parameter for numbers  
    """
    answer = h + y
    return answer


print(example2(1,2))



"""
    Why is knowing the function signature important? Well it's going to be one of those factoids thatr
    randomly shows up on interviews.
    
    Secondly, it acts as a way of summarizing what a function does 
"""


"""
    Mutability Review: 
    
    Things on a computer have different types of changability.
    
    Mutability = the degree by which something can change 
    
    This is actually binary in choice, its either mutable or immutable
    
    things that are mutable = can change
    things that are immutable = can't change 

    examples of things that cant change:
        1. numbers: integers, floats, etc.
        2. booleans: True or False
        3. Basically every primitive data type
        
    examples of things that can change:
        1. lists
        2. Strings
        3. dictionaries
        
    What do i mean by things that can't change
"""


GPA = 0 #< Everytime we wanted to update this value, we had to do another variable reassignment

#GPA = something else
#in this case, GPA = GPA + current grade 

"""
    Things in python that are immutable require another reassignment to change the value.
    
    How do we know that lists and dictionaries are mutable by comparison?
"""

mylist = [1,2,3]
print(mylist)
mylist.append(4)
print(mylist)

""" 
    WE did not do another variable assignment to update our list, we just updated it with .append()
    That implies that something about the attributes of the list can change without having to do
    mylist = again


    So why exactly do we care about immutability?


    The example you should be most familiar at this point is with dictionaries:
    
    Keys = immutable < keys are addresses, how annoying would it be if you got a new piece of furniturre
    and the address of your house changed
    
    Why else do we care? the parameters we pass into a function greatly determine the behavior 
    of said function if the parameters are mutable or immutable 
"""


mylist2 = [1,2,3,4]
def addone(list):
    list.append(5)
    
addone(mylist2)
print(mylist2)

#lists ARE mutable, and when we passed it into a function, it did not delete itself after the function
#call was over
x = 1
def addoneagain(num):
    num = num + 1
print(x) 
"""
    Numbers are Immutable, something weird happened here. The weird thing that happened here is what we call
    Pass by Value vs Pass by Reference
    
    
    Think of every variable (lists, strings, dictionaries, numbers) as being two pieces of information 
        1. The name of the variable
        2. the data stored at the variable
        
        You have to think that the name of a variable as also an address in memory. 
        
    multiple things at play here:
    
        Immutable Variables are passed by value into functions
            when I did addoneagain(x), and had x = 1.
            x was not passed into the function, only 1 was. 
        Mutable Variables are passed by reference into functions 
            When I passed in mylist2 into addone(list)
            the reference to mylist2 was passed into the function and not the values of the list 
            
        This dichotomy is how functions interact with mutable/immutable objects in pretty much
        every programming language ever 
        
        If you really wanted to think about it,
        
        pass by reference = is passing in the left hand side of the variable
        pass by value = passing in the right hand side 
"""

"""
    Functions seem to have a lot of baggage involved. You've also seen at this point that functions are useful in various ways
        1. reusability - in lab 5, you called calculateGPA in your check honor roll function rather than just writing the calcgpa function again
        2. basically designs your program for you - think of function headers as tasks or chapter titles
        
    but also in practice, software development is not done in one file over tens of thousands of lines of code. So how do functions become usefl
    over multiple files? 
    
    
    Python (and pretty much every programming language ever) allows for the importing of other python files.
    
    In this scenario, we have certain behaviors that we always want to repeat. So why would we keep rewriting a mean function when we can just 
    import the behavior automatically and only write it one time ever in our life 
"""

import notes.functions.helpfunctionsforstatistics as help

mylist = [2,5,6,7,9]
avg = help.getMean(mylist)
print(avg)

"""
    import keyword allows us to use functionalities from other python files in the one we're working on.
    
    So what are some nuances to import
    
    Whenever you want to use a function from another file, what you should do is 
    
    <name of file>.<name of function>(<parameters if there are any>)
    
    Are there any other nuances? I have to type the filename as written whenever i want to use a function from another file
    
    That sounds horrible because filenames can get long. So the "as" keyword allows me to temporarily rename the file 
    
"""

