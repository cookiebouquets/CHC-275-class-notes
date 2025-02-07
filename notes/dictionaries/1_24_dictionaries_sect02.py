"""
    Today we are covering dictionaries.
    
    I'm going to try something new today, it's called live coding where  i code on the screen 
    in real time and type in my notes intermittently 
"""


"""
    Question: How would store multiple pieces of information with what we know? 
    Answer: You would use a list  
"""


"""
    Lists have one problem, if the contents of the list are not known to us as the user, 
    then we are going to have a hard time finding something that we want. If you wanted to find something 
    out of a list, you would need to do a search algorithm. 
    
    This is computationally very expensive. Naively, we can search over the entire list but that is not
    good because we have a potential to run a for loop for len(list) times.
    
    Dictionaries fix this by basically assigning every element to a "look-upable" address
"""


"""
    Dictionaries are basically just lists, but rather than having indices from 0,...,len(list) -1,
    we assign each individual value to a key that we can look up.
"""

my_dict = {}
my_dict2 = dict()

"""
    The syntax for dictionaries is curly braces. To add elements they follow the following syntax
"""

my_dict3 = {"key":1, "key2":2, "key3":3}    
            #key #value 
"""
    All things in dictionaries follow the template of {key:value, key:value,}
"""

"""
    How do we access things from dictionaries?
"""

print(my_dict3["key"])
print(my_dict3["key2"])

"""
    What can be a key? Values can be anything, it doesn't really matter what you store in a value
    but keys have to be something that is called immutable
    
    immutable = things in code that cannot be changed. Ex. basic data types: strings, ints, floats
    
    
"""
def add():
    num = 1
    num2 = 3
    sum = 0
    print(sum)
    sum = num + num2
    print(sum)



"""
    So in this example, sum was immutable because in order to change the value, we had to do another variable
    assignment. something that is not immutable are lists
"""

def changelist():
    mylist = [1,2,3]
    print(mylist)
    mylist.append(4)
    print(mylist)
    
"""
    So lists are mutable, we didn't have to do another variable reassignment to add 4 to our list
"""


"""
    Why do keys need to be immutable? Imagine you live in a house. Every time you change the key 
    to your house, your house is teleported to a new street. So keys for dictionaries have to be immutable
    because if they weren't, your values would move around in memory every time you updated the key
"""
def keytest():
    my_dict4 = {"af":313, 14:"hello", 3.14: "pi"}

    print(my_dict4["af"])
    print(my_dict4[3.14])


"""
    How do we solve our searching problem from earlier?
"""

def searchdict():
    my_dict4 = {"af":313, 14:"hello", 3.14: "pi"}
    if 313 in my_dict4:
        print("That is in the dictionary")
    else:
        print("that is not in the dictionary")
        

        
"""
    the "in" keyword searches for KEYS and not VALUES. So as mentioned earlier, anything can be a value,
    including lists
"""

def usertest():
    users = {"basmacij":["password",12,"basmacij@calverthall.com"],"cardinalg25":["ilovechc",9,"cardinalg25@chcstudent.com"]}
    print("password, gradelevel, email")
    print(users["basmacij"])

    print("password is " + users["basmacij"][0])

"""
    We made a dictionary comprising of keys (usernames) and values (account information)
    The values were lists of objects
    to access objects in a list at a certain key, the syntax is
    
    my_dict[key][index]
    
    Next thing we want to think about: Loops over dicts. What we have for lists are 
    
    for-each or for-i (index) loops
    
    dictionaries work basically the same way, but we want to make the distinction that for-each
    specifically iterates over keys.
"""

def looptest(dict):
    for x in dict:
        print(x)
        print(dict[x])


looptest(my_dict3)


"""
    For each loops iterate over keys, so to get the values make sure you square brackets operator
    the current key you're at.
    
    How do we add to a dictionary. Conventional wisdom is .append(key,value) but dictionaries dont have
    that function. 
    
    What you have to do, is a variable assignment with square brackets
    
    ex. mydict[newkey] = newvalue
"""

my_dict3["key4"] = 4
print(my_dict3["key4"])


"""
    That also means you update dictionary values the same way.
"""

my_dict3["key3"] = 1
print(my_dict3["key3"])

"""
    When we were working with lists,  when we tried to access a list at an index that doesn't exist,
    we'd get an index error. 
    
    If we try this for a dict, we're gonna get a keyerror
"""

#print(my_dict3["key5"])


"""
    useful to mention functions for dict: .keys() and .values()
    
    .keys() returns a list of all of the keys without their values
    .values() returns a list of all of the values without their keys
"""

print(my_dict3.keys())
print(my_dict3.values())

"""
    Before we leave, for vocab purposes, python dictionaries are also called hashes, hashtables, hashmaps
"""

