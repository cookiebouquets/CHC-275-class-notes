"""
    Our goal for the next cycle is to cover multiple files (modules) and 2d lists 
    
    Today we're going to cover modules
"""


"""
    for reference: Lab 6 is going to be mancala so 2d lists are going to be important there
    and also modules will be important just in general for programming 

    In the real world, not everyone works on one file. If apps were built on only one file you would have
    like 10 thousand lines of code. This is not the most ideal for multiple reasons
    
        1) verison  control - If i accidentally delete that one file its over 
        2) Repeated services across multiple apps - if one file corresponds to one service,
        then you can import that service to other apps. 
        3) same deal as functions, we want to enforce reusable code
"""

""" 
    The idea is, that apps are stored in shared folder and python files
    can interact with each other as long as they're in the same folder
    
    1) statistics is useful and not really limited to one project
    2) rather than rewriting a bunch of code for each statistics function, we can just 
    import the file file into the one we're working on and use the behaviors from the imported file
"""

""" 
    How do we import files? 
    
    We can use the import 
"""

import helpfunctionsforstatistics

mylist = [1,4,56,3,67,7,2]

""" 
    To use functions in other files after importing them, you use the syntax
    
    <file name>.<function>(parameters) 
"""


print(helpfunctionsforstatistics.getMean(mylist))


""" 
    So that implies that we can have a collection of python files interacting with each other
    
    That means you can have seperate files for different business/school/etc. functions that 
    indiviuals who specialize in that field can work on their own code and import what they worked
    on into the main app.
"""

""" 
    the imported file is a python module (packages)
    
        - fileinput 
        - tensorflow (machine learning/AI)
        - scikitlearn (this is the one for statistics)
        - matplotlib (this one makes graphs)
        - pygame (game package for python)
    
    
    other things syntactically that are important:
    
        - we can rename modules temporarily
"""

import helpfunctionsforstatistics as help 

"""
    the "as" keyword will rename the file locally so you dont have to type in the full file name
"""

print(help.getMax(mylist))


""" 
    Other things you can do
    
        - you can specifically import one function from a file 
        
    loading in python modules takes up a lot of RAM on our computer. So in cases where
    our project calls for different functionalities from a lot of different modules, then we 
    can specifically import the behaviors we want
"""

from helpfunctionsforstatistics import getMedian

"""

    from <file> import <function> will import the specific function that you want from your package
    
    additionally, i dont even need to do
    
    helpfunctionsforstatiscs.getmedian 
    
    or
    
    help.getmedian 
"""

print(getMedian(mylist))

""" 
    So the idea as a programmer is to write super generic code that can be reused across 
    multiple projects and never have to rewrite code we've already written 
    
    I can also import from nested folders
    
    folder topology is 
    
    testfunctions -> all of our files + another folder 
    
    specifictests -> goofy.py
    
    the syntax for pulling a module from another folder is 
    
    <top level>.<every other level>.<filename>
    
    from <folder> import <module>
"""

from specifictests import goofy

goofy.hello()

""" 
    That is basically all i have to say about modules. You can practice working on this by making a folder and multiple python files
    and working on them individually and importing them all at the end.
"""