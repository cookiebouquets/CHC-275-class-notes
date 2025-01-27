"""
    Today we'll be covering dictionaries. 
    
    From now on I'll be doing what is called live coding. Rather than making slides,
    I will write my notes as comments in a python file so that you can see running  code alongside 
    my annotated notes. 
    
    I have also made a github repo for the class. You can find all lab templates and notes there. 
    The link was messaged to you on blackbaud. 
"""

"""
    Some Announcements: Tomorrow in day 2, I'm going to release lab 5. It's going to be about the
    content covered today.
    
    We're cover dictionaries. In other languages, they're usually called hashmaps, hashtables, or hashes
    
    Guiding question: If you wanted to find something in a list, you would have to iterate over a list
    using a for loop. the most consistent way to look something up, is to use a dictionary
"""

mydict = {}
mydict2 = dict()

"""
What goes inside a dictioinary vs a list?

Lists have two pieces of information associated with them. 

index = position of the list
value = item stored at the index

dictionaries have 

keys = which are addresses to values
values = items associated to keys 
"""

mydict = {"key1":1, "key2":2, "key3": 3}
#syntax  {key : value, key: value, key: value}
print(mydict)
print(mydict["key2"])

"""
    What exactly can a key be? Obviously at least strings, but what other data types?
    
    VOCAB WORD: 
    
    Immuatble = objects that cannot by changed 
    examples: strings, integers, floats
"""

def add(x,y):
    sum = 0
    sum = x + y
    return sum


"""
    Any time you have to a variable reassignment (use a equals sign), that object is immutable. 
    What is not an immutable object? 
    
    Lists, or other dictionaries
 
"""

def updateList(list):
    value = 1
    list.append(value)

"""
    Lists by comparison are mutable. Why do we want keys to be immutable? 
    
    If your value lived in a home, then your key being mutable would be equivalent to your key
    opening the door of a different house every time you changed the key in some way
    
    How do we update dictionaries?
"""


#adding to a dictionary
mydict2["key4"] = 4
#the syntax has changed, before we just did list.append(value), but now we have to do
#dict[newkey] = newvalue
print(mydict2["key4"])


#deleting from a dictionary
mydict2.pop("key4")
#dict.pop(key) deletes things from dictionaries
#we should get a key error here 

"""
    Keys are unique, values are not unique. So therefore, one key corresponds to exactly one value
    so for example, if I had a key  called key 1, then key 1 has exactly one value
    
    dict[key1] = value1 
    dict[key1] = value2
    
    would just update key1 and lose value1 into the void. That also means,
    
    dict[key1] = value1
    dict[key2] = value1
    
    is ok, two keys can have the same value. How do we loop over a dictionary?
"""

for key in mydict:
    print(key)

"""
    for loops specifically iterate over keys, and not values. How would we access each value?
"""

for key in mydict:
    print(mydict[key])
    
    
    
"""
    Additionally, the in keyword also works for if statements. It primarily searches for keys
    
    if key in dict
"""

if "key1" in mydict:
    print("That is a key")
else:
    print("that is not a key")
    
if 1 in mydict:
    print("That is a value")
else:
    print("Remember! the in keyword searches for keys")
    
    
"""
    We spent a lot of time talking about keys, but what can values be?
    Values can be (mostly) anything, so integers, floats, dictionaries, and lists
"""

mydict["list"] = [5,6,7]
print(mydict["list"])

"""
    Scenario: If you had a dictionary of students, then their key corresponding to their grades, should
    point to a value that is a list of their grades
    
    How do we access individual elements of a list that is stored in a dictionary?
    
"""

print(mydict["list"][2])

#the syntax is dictionary[key][index] for Lists or dictionary[key][key] for dictionaries

mydict["list"].append(8)

print(mydict["list"])
print(mydict)

""" 
    Important functions to know
    
    .keys() returns a weird object that we should convert into a list. That list will then become
    a list of the keys.
    
    .values() returns the same weird object, convert it to al ist, and it willbe a list of values
"""

keys = mydict.keys()
print(keys)
#what is a dict_keys object? I have no clue
keys = list(mydict.keys())
print(keys)
#use the list keyword to convert dict_keys into a list

values = mydict.values()
print(values)
#what is a dict_values object? I have no clue
values = list(mydict.values())
print(values)


"""
    Philsophically why do we need dictionaries over regular lists? If we think about the bank lab,
    The way we did it was by making two concurrent lists and keeping track of the indices. 
    Dictionaries remove that requirement of having two lists, and now we can store the values at a named
    address which makes sense to our program design
    
    So for example, a bank account before had two lists
    
    ["name","balance"] and now has one dictionary {name:"name", balance,:balance}
"""


"""
    Helpful for the lab, you can return multiple things at once
"""

def first_second(mylist):
    return mylist[0],mylist[1]

#return two values, separated by a comma
testlist=[ 1,2,3]
var1,var2 = first_second(testlist)
print(var1)
print(var2)

#convention is declaration of variables are assigned in the same order as the return statement