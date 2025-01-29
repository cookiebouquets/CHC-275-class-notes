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
    
main()
    
    
"""
    How do we save var1? 
    
    That is the whole purpose of the return keyword 
    What return does is flag the computer to save the thing after the return keyword 
    The thing is, you now have to save that result into a variable in the scope outside of it 
"""