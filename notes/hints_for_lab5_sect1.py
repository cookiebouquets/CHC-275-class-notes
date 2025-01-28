"""
    Hints for lab 5
"""

"""
    Student records are dictionaries of dictionaries. So how do we get "a" from the nested dictionary
    list[index]
    dict[key]
    
    whenever there is a list of a list or a dictionary of a dictionary or some combination of those, all you have to do, is add a second
    set of square brackets
"""

mydict = {"key1" : {"keya" :"a", "keyb": "b"}}
print(mydict["key1"]["keya"])

"""
    The syntax is mydict[key1][key1_1]
"""


""" 
    When doing lab 5, i'd do the functions in this order
    1. printMenu()
    2. addStudent()
    3. removeStudent()
    4. CalculateGPA()/changeGrades()
    5. checkHonorRoll()
    6-9. all of the get functions 
"""


"""" 
    Also, I'll show you fstrings right now
"""

var1 = 5

print("Var1: " + str(var1))
print(f"var1: {var1}")


""" 
    fstrings allow you to print variables in line with text without having to typecast your variable a string.
    
    The syntax is 
    
    print(f"message {variable name}")
"""


""" 
    In programming, a computer science mindset is to break down a problem into smaller parts and all them all up.
    addStudent() has a lot going on. So what you should do 
    
        1. make a variable called studentname which takes in the input for a name
        2. make a dictionary called grades = {"math" :0, "english" :0, "religion" : 0, "History" : 0} set all values to 0
        3. for - loop over the grades dictionary and update the grades
        4. make a variable called gradelevel which is the student's grade level
        5. make a variable called email which is a string for the email
        6. student = {"grades": grades, "grade level" : gradelevel, "email": email}
        
        7. directory[studentname] = student
        
"""