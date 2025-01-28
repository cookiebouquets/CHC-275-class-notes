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

