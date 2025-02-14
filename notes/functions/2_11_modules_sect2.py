""" 
Today we will continue our discussion on multiple files and importing

For juniors: Course Recommendations are live, see me if you wish to discuss next year for 277 or 280.


277: Introduction to Computer Algorithms 

    This class is basically CMSC 202 + very basic CMSC 341 at UMBC, will be taught in either Java or C++. Will cover 
    object oriented design, asymptotic analysis (at a deeper level than this course will provide),
    very basic data structures (linkedlists, binary trees) and algorithms (breadth first, depth first, greedy). 
    This class will be very good for those going on to study Computer Science or any CS related field in college, 
    you will learn a lot of very advanced topics a lot earlier than you will see them in college 
    and will set you up for success in the difficult courses in those degree programs. 
    
    I'd recommend this course to the extremely motivated.

280: Cybersecurity Essentials

    This class is getting a redesign next year. It will basically follow this plan:
    
    1st semester will be all on computer networks and protocols, teaching you the language of information
    technology. 
    
    2nd semester will then be on practical cybersecurity based on the concepts you learned in the first
    semester, i.e. you need to be familiar with the vocabulary and concepts in a perfect setting
    before you learn about what vulnerabilities are possible.
    
    I'd recommend this course to either Prep B guys are people looking for a lower stakes elective. 
"""

""" 
Last time we talked about importing files. 

    1) allows for easy collaboration
    2) allows for extreme reusability of code - we want this in particular
    3) also is the most basic version of Objected Oriented Inheritance <- we'll talk about this later
    
    
    recall: 
    
    1) we have to be in the working directory where every file is stored. (every being the one you want to import and also 
    the one you're working on)
    2) you need to use the import keyword
    3) you can either import one function, multiple functions, or all of them
    4) you can rename the file 
    
    keywords: These are modules in python 
"""

import notes.functions.testfunctions.helpfunctionsforstatistics as helpfunctionsforstatistics
import notes.functions.testfunctions.specifictests.goofy
import testfunctions.test

mylist = [1,2,3,4,5]

print(helpfunctionsforstatistics.getMean(mylist))

""" 
this is how you import things in a very basic fashion.

Other things we can do: we can rename the file temporarily 
"""


import notes.functions.testfunctions.helpfunctionsforstatistics as stats

print(stats.getMax(mylist))

"""
We can also import specific functions into our file
"""

from notes.functions.testfunctions.helpfunctionsforstatistics import getMedian

print(getMedian(mylist))

""" 
So the original syntax was 

<other file name>.<function> 

but if we import specifically one or more functions, we can just call the function as if it was already built into python
"""

from notes.functions.testfunctions.helpfunctionsforstatistics import getMax,getMin

print(getMax(mylist))
print(getMin(mylist))


""" 
The question we want to have answered is:

    In our organization, we don't have certain permissions on seeing certain files in other folders,
    
    i.e. the file we're currently working on is in a separate folder from the module we wish to import 
"""

import sys 
sys.path.insert(0,"../testfunctions")
import testfunctions

testfunctions.test.example()

""" 
So to import from another folder, all we need to is use the sys module and open the path using sys.path.inset(0,"pathname")
then, we should be able to import the file as folder.filename 
"""



"""
So let's test for multiple files in this one folder.

If I just import the entire folder, we should get access to .test and .goofy
"""

import testfunctions

testfunctions.test.example()
notes.functions.testfunctions.specifictests.goofy.hello()

"""
So we got both files from just importing the folder. A collection of files is still called a module or a package
(in other languages)
"""


""" 
So we covered modules today, expect to see it in lab 6
"""