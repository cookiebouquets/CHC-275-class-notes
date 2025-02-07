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

#FEB 4, DAY 1

""" 
    ANNOUNCEMENT: I'm moving the due date by a whole cycle basically. 
    
    If I were you, if you're starting from 0:
    
    1. download the template and just edit that file 
    2. do printmenu()
    3. Do add student
    
    
    By today, you should have printmenu() and addstudent() done.

"""

"""
    So the easiest way to do add student
     
        1. Just get the studentname
        2. get the email
        3. get the grade level
        4. make a dictionary called grades
            4a. grades = {"math":0,"english":0,"history":0,"religion":0}
            4b. for loop over grades
                4i. in your for loop, update each individual grade
        5. directory[studentname] = {"grades":grades, "email":email,"gradelevel":gradelevel }
"""

#FEB 5, DAY 2

"""
    Today you should work on CalculateGPA and checkHonorRoll
    
    The real question we have for calculate GPA is how do you get the grade data
    out of the student dictionary
    
    directory = all students
    students = grades, grade level, email
    grades = subjects and their grades
    
    You're going to have to use square brackets
    
    
    for calculate GPA, there are two parameters, directory and student and to access
    "nested" data, all you need to do is use a second and third set of square brackets
    
    dict[key] will return value
    
    if value was also a dictionary you would just this 
    
    dict[key][value] will return the value at value
    
    directory[student]["grades"] <== for loop over this and add up the GPA
    
    so after forloop and add to GPA,
    return GPA/4
""" 