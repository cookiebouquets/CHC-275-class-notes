"""
    Hints for Lab 5
"""

"""
    1. printMenu()
    2. addStudent(directory) 
    3. calculateGPA(directory, Student)
    4. checkHonorRoll(directory,Student)
    5. literally everything else 
    
    So today 1/30 we're gonna talk about addStudent()
"""


""" 
    each student is a dictionary
    we make a empty dictionary using {}
    
    doing everything in one line is basically impossible
    
        1. Student = {"grades" : grades, "grade level" : gradelevel, "email" : email}
            a. so do gradelevel and email first
            
            question: how do we make a variable
            
            <name> = <data>
            
            question: How do we accept keyboard input
            
            we only need input()
            
            does input() accept an argument? yes, the question that gets asked to the user
            
            what is the return type for input. It's a string
            
            gradelevel - integer
            email - string
            
            
            how do we convert a string to an integer. We can typecast the string
            
            int() 
            
            gradelevel = int(input("enter your grade level ")
            email = input("enter your email ")

            
"""

#gradelevel = int(input("enter your grade "))
#email = input("enter your email")

"""
    for grades:
    
    there are only four classes you can take math, history, religion, and english
    
    
    we can just preload the dictionary with the class and set all of the values equal to 0 
    
"""

grades = {"math":0, "english":0, "religion":0,"history":0}

"""
    Thought question:
    
    How do we iterate over every element of a list or dictionary?
    
    we agree its going to be a for loop.
    
    Concept check: 
    
    What does a for loop over dictionaries pull out? keys or values? Keys
    
    for ___ in grades 
    
    
    How do we access a value from a dictionary 
    
    grade[key] = 
"""


#for subject in grades: 
    #grades[subject] = int(input(f"enter the grade for {subject}: "))
    
    
    
"""
    f-strings let you print a variable in line with a string
    
    you put f before the quotations and then the name of the variable you want to print in the curly
    braces 
"""


#JAN 31, DAY 5            

"""
    by now you should have 
    
    1) print menu
    2) add student done
    
    the next logical things to do are 
    
    3) calculate GPA
    4) check Honor Roll
    
    
    So GPA is just unweighted average over the number of courses. < Lab4
    
    
    so what you might not know how to do is how to access a dictionary inside a dictionary
"""

testdict = {1:[5,6,7],2:[1,2,3]}

"""
    So the question is, how do we get the values out of the dictionary at key 1.
    The way you do this, is with multiple square brackets
"""

print(testdict[1][0])

"""
    When you want to access a sub-dictionary or sub-list, you need to add a second set of square brackets
    so in general
    dict[key][key]
    dict[key][index]
    list[index][index]
    etc. 
    
    student[grades][course] <== this is how you pull the grades out of the student dictionary
"""