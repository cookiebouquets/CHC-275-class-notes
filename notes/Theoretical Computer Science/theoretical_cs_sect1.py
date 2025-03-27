""" 
Theoretical Computer Science - Asymptotic Analysis 

What asymptotic analysis does is analyze the runtimes of the computer programs we write 

Typically we want programs that are pretty quick. There are three main categories of algortihms in terms 
of  their runtime

1) Internet Ready - Stuff that can be ran within seconds
2) Weather Predicition - Stuff that takes days or up to weeks to run
3) totally unfeasible to run in the slightest - Will take multiple lifetimes to run

Typically as good computer programmers/scientists, we want our algorithms/programs to fall roughly
in category 1 or category 2.

Asymptotic Analysis is the main tool of the next class in this sequence, if you're taking 277,
you're going to see this the entire class basically
"""

""" 
What is the main tool of asymptotic analysis? 

Big-O and what it does, is characterizes general algorithms into certain buckets based on their characteristics


There are two main things we care about when analyzing the behavior of functions

1) The input size matters (lengths of lists, lengths of strings, lengths of 2dlists, etc.)
2) How long it takes for the function do to the thing its meant to do (run time)

You can think Big-O as being a function of lengths that outputs runtimes

For example 

Let's we have a list of numbers of length 10, we want to add "1" to each individual entry of the list

What is the input size? 10 (the length of the list)
What is the runtime? It would be 10 executions (How many times something was done)

There is no general agreed upon time "unit" for the runtime of algorithms because it dependent on hardware

This example was what's considered the local behavior of that function. We care about the global behavior

What happens if the list is of length 5?

input size: 5
run time: 5 executions

The point is, no matter what choice of input size for this function, the runtime is the same length as the
length of the initial input 


We say that this algorithm has O(n) runtime complexity. The reason why:

if we call our list length n, then the runtime will end up being the same legnth of the list (n)


"""

def myfunction(list):
    #This function is O(n)
    for i in range(len(list)):
        print(i)
        
#myfunction([1,2,3,4])

def myfunction2(list):
    #This function is also O(n)
    for i in range(len(list)):
        list[i] = list[i]*15
        print(list[i])
        
#myfunction2([1,2,3,4])

""" 
Myfunction and myfunction2 are basically the same function theoretically. They both have the same input 
size and the same runtime complexity

What happens if we did a nested for loop?
"""

def myfunction3(list):
    for i in range(len(list)):
        for j in range(len(list)):
            print(i + j)

#What is the input size of this function? n
#What would be the runtime complexity? Let's do an example run

""" 
Let's say our list was [1,2,3]

first run of i-loop
    first run of j-loop
        1+1 = 2
    second run of j-loop
        1+2 = 3
    third run of j-loop 
        1+3 = 4
        
second run of j-loop
    first run of j-loop
        2+1 = 3
    second run of j-loop
        2+2 = 4
    third run of j-loop 
        2+3 = 5
        
third run of j-loop
    first run of j-loop
        3+1 = 4
    second run of j-loop
        3+2 = 5
    third run of j-loop 
        3+3 = 6

So each for loop has a subprocess of 3 lines
and there are 3 i-loops

O(n^2) is our runtime complexity.

The question is: Which is more preferable, an algorithm with O(n) complexity or O(n^2). The algorithm
with a higher power takes longer to run. So we want the smallest power possible in our algorithm 

So if you looked at myfunction3, the runtime complexity was n*n, two nested for loops. What about if we took
the square root of both lengths first
"""

def myfunction4(list):
    print("Square Rooted Lists")
    for i in range(int(len(list)**(1/2))): #This is the same thing as taking the square root
        for j in range(int(len(list)**(1/2))):
            print(i + j)

myfunction4([1,2,3,4])

""" 
The question was, what happens if we take the square root of the length?

IF we did this with just one for loop, our runtime complexity would be 

O(sqrt(n)), but what happens if we do a nested for-loop

O(sqrt(n)*(sqrt(n))) = O(n)

So nested forloops actually just multiply the length of the lists together in terms of complexity


"""

def myfunction5(list):
    print("Normal List and SquareRooted List")
    for i in range(len(list)): #This is the same thing as taking the square root
        for j in range(int(len(list)**(1/2))):
            print(i + j)

myfunction5([1,2])

""" 
In this example, we took a list of length n and did a nested forloop with a list of length sqrt(n) 

We gotta save this for another time 
"""

"""
We discussed multipicatively what happens with Big-O, what happens when we add things together
"""

def myfunction6(list):
    print("adding loops together")
    for i in range(len(list)):
        print(i)
        
    for j in range(len(list)):
        print(j)
        
""" 
When we add loops together, it's the same thing as adding n to itself.

myfunction6 has a runtime complexity of O(2n), because it's the same thing as O(n + n).

"""

myfunction6([1,2,3])

""" 
The thing is, runtime complexities that differ by a constant are considered the same function mathematiically.

So myfunction and myfunction6 have the same runtime complexity because they differ by a constant of 2,
  
O(n) vs O(2n)
"""

def myfunction7(list):
    print("Nested For loop + Regular one")
    for i in range(len(list)):
        for j in range(len(list)):
            print(i + j)
            
    for i in range(len(list)):
        print(i)
        

""" 
myfunction7 has two nested forloops and a regular forloops so it has a total runtime complexity of \

(n*n) + n = n^2 + n

The same thing matters here, myfunction7 is really just a O(n^2) function, even though its actual
runtime complexity is O(n^2+n)

Constants don't matter really

and also

the biggest power wins 

when it comes to analyzing the behavior of functions
"""

""" 
Common runtimes that will come up

O(1) <= This is called Constant Time
O(n) <= Linear Time
O(n^2) 
O(n log n) <= Logarithmic time

In order:

O(1) is most preferable, because there is no dependency on the size of the list
O(n) is next most preferable 
O(n log n) is next most preferable
O(n^2) is typically considered very bad
"""

#MAR 25, DAY 2
""" 
Today we're going to cover recursion

Basically what recursion is = just a function that calls itself.

Vocab Review:

Function call = When you use the function in the body of another code block

print() is a function call

list.append() is a function call

a function that is recursive is a function that calls itself.

The easiest example of this is a countdown
"""


"""
For every recursive function, you need to have a base case, because if you don't 
you have no way of exiting the recursive function.

Just like in a while loop, you need a way to escape the code block
"""

    
"""
Let's do n = 5

n = 5
if n < 1 
    return 0 <== this isn't happening
    
print(time)
return countdown(5-1)

n = 4
if n < 1 
    return 0 <== this isn't happening
    
print(time)
return countdown(4-1)
.
.
.
n = 0 
if n < 1 
    return 0 <= now it will work
"""

def countdown(n):
    if n < 1:
        return 0
    
    print(f"T = {n}")
    return countdown(n-1)

countdown(5)

""" 
So countdown is the most basic example of recursion, there are more less obvious
examples.

Factorial is 

x! = (x)*(x-1)*(x-2)*...*1
x! = x *(x-1)!


What is the base case for factorial:

0! = 1
"""
def factorial(n):
    #Base Case
    if n == 0:
        return 1
    #Recursive Case
    temp = n * factorial(n-1)
    
    #Returning Result at the end
    return temp
    
print(factorial(5))

""" 
The best way to think about recursion is like a ladder

in our factorial case, we're returning temp as the answer of our overall factorial
and then we go down the ladder for every n-1 up until 0

n = 5

5 * factorial(5 -1 ) - > 4*factorial(4-1) - > 1*factorial(0) <= this is going down

1*1 * 2*1 * 3*1 *4*1 *5*1 -> Going back up the ladder

So understanding how recursion works is really hard, you kinda just have to 
implement it a bunch of times until you get it to work properly in your mind

it's an experience thing
"""

""" 
The next recursive operation that you've probably heard of is the fibonacci numbers

fib(n) is a function 

base case
fib(0) = 1
fib(1) = 1

fib(n) = fib(n-1) + fib(n-2)

fib(0) = 1
fib(1) = 1
fib(2) = fib(1) + fib(0) = 2
fib(3) = fib(2) + fib(1) = 2 + 1 = 3 
fib(4) = fib(3) + fib(2) = 3 + 2 = 5
.
.
.

""" 
def fib(n):
    #Base Case
    if n in [0,1]:
        return 1
    else:
        #Recursive Case
        return fib(n-1) + fib(n-2)
        
print("fib")
print(fib(4))

""" 
This is our fibonacci sequence.

countdown, factorial, fibonacci sequence are things you wouldn't see in practice

Where recursion really comes up is in pathfinding algorithms <- this is why
we spent a lot of time on asymptotic analysis and why there's a whole class on it 
next year.


"""


BOARD = [ 
             [0,1,1,1,0,0,0],
             [0,1,0,1,1,0,0],
             [0,0,0,0,0,1,0],
             [0,0,1,1,0,0,1],
             [0,1,0,0,1,0,1],
             [0,1,0,0,1,0,0],        
    ]

"""
We're going to do a basic pathfinding algorithm. 

We're going to have these postulates (A postulate is an assumption):
    1) 0s are open space. We can pass through 0s.
    2) The edges of the board are places you can't cross. So you can't fall off
    the end of the board
    3) We want to find X 
    
So if we were to write an algorithm to do this:

The naive way is to just search each piece of the board. There's one problem what
happens if X is the very last entry 


             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,"X"],  

We'd have to search the entire board. Searching a 2dlist in its entirety is O(n^2)

for row:
    for col:
    
The question is: Is there a better way? 

    1)Pick a coordinate on the board on the board
    2)Recursively search in the Y direction
    3)If you don't find it, recursively search in the X direction
    4)If you don't find it after that, pick a different coordinate and do it again
    

This algorithm should be faster than searching the whole board, because if we pick the
coordinate where the X lies in the row or column that we selected, then we'd only
have to search at most 12 elements

The idea is, on average this algorithm should perform better than searching the entire
board.
"""

#RECURSION DAY 2
""" 
Today we're going to go over more examples of recursion (and also attempt to do the grid search algorithm
again).

The next thing we're going to do is palindrome.

We've done palindrome before: we're just confirming whether or not a word is a palindrome. 

A palindrome = A word that is spelled the same way backwards

RACECAR
TACOCAT

The original palindrome algorithm that we wrote:

    1. Input word
    2. Create a new variable and saved the reversed word into this variable
    3. check if the word = reversed word
    
    
There are some technical considerations:

    1. Time complexity: Palindrome done this way is O(2n)
        a. We have take our word and reverse it (One for loop)
        b. We have to a second for loop and check character by character if the word is a palindrome (n + n)
        
    2. Memory Complexity: We had to instantiate a seperate variable entirely in order to have something to
    compare to 
        a. effectively doubling the memory requirement of our program
        
        
If we do this recursively 

    1. We should have the same time complexity O(n)
    2. We don't need to make another variable
        
"""

def iterpalindrome(word):
    #Regular Palindrome
    reverse = ""
    for char in word:
        reverse = char + reverse
    
    if reverse == word:
        return True
    else:
        return False
    
print("Iterative Palindrome:")
print(iterpalindrome("tacocat"))

""" 
Now if we want to do it recursively, all we have to do is compare the beginning and end of the string
and compare the next two ... up until the end

abcdcba
a     a
 b   b
  c c
   d
   
basecase: Check the middle letter and just return true

recursive case: check the ends of each substring
"""

def recursivepalindrome(word):
    #Base Case
    if len(word) == 1:
        return True
    
    
    #Recursive Case
    if word[0] == word[len(word) -1]: 
        return recursivepalindrome(word[1:len(word) - 1])
    else:
        return False

print("Recursive Palindrome: ")
print(recursivepalindrome("racecar"))

""" 
So our recursive palindrome works differently than our iterative palindrome. 

1. We use the same time complexity
2. We use a better space complexity because we don't make a separate variable for the reversed word.


Last class we talked grid search

our objective was find the X in the list. This time I'm going to create a maze and what I want to do is 
return the path that leads to the exit.

We're starting from the top left and the exit is the bottom right. and we want to return the path
that gives us a way to the exit
"""

""" 
Return a path that takes us from top left to bottom right recursively, we only need to go in two directions
down and to the right

What we want to do is make a list called path and just remove the elements that don't end up in the right spot


"""
BOARD = [ 
             [0,1,1,1,0,0,0],
             [0,1,0,1,1,0,0],
             [0,0,0,0,0,1,0],
             [0,0,1,1,0,0,1],
             [0,1,0,0,1,0,1],
             [0,1,0,0,1,0,0],        
    ]


def valid_move(x,y,BOARD):
    #Valid move is going to return true if the move is valid
    #A Valid move is one that doesn't go off the edges of the board and doesn't hit a 1
    return 0 <= x < len(BOARD) and 0 <= y < len(BOARD[0]) and BOARD[x][y] == 0

def pathfind(x,y,BOARD,path):
    #This is our Recursive Function
    
    #BASE CASE, if we make to the bottom right we just append that coord to the list
    if x == len(BOARD) -1 and y == len(BOARD[0]) -1:
        path.append((x,y))
        return True
        
    #RECURSIVE CASES, down first 
    if valid_move(x,y,BOARD):
        path.append((x,y))
        
        #Down Case
        if pathfind(x+1,y,BOARD,path):
            return True
    
        #Right Cased
        if pathfind(x,y+1,BOARD,path):
            return True

        #If the move isn't valid, backtrack 
        path.pop()
    return False
    

def gridsearch(Board):
    path = []
    if pathfind(0,0,Board,path):
        return path
    else:
        return "Path not found"


print(f"Path: {gridsearch(BOARD)}")
""" 
Our print statement printed the valid path for our maze recursively. This is usually the biggest application
of recursion 

LAB 8: Labrynth

Our goal is to have two path findings at the same time in LAB 8

The person trying to escape: This person is trying to go from the the top left down to the bottom right 

The minotaur: Start in the center and try to intercept the person trying to escape

If the minotaur reaches the spot the person is going to, then the minotaur wins, but if the person
gets to the end then the person wins.

The minotaur will go in random directions around the labrynth to simulate AI, and the person will use an 
optimal path finding algorithm. 

LAB 8 is definitely going to be the hardest lab and its the last lab of the class
"""


#MARCH 27, DAY 4
""" 
Today we're going to cover object oriented programming

So Object Oriented Programming was invented in probably the 80s and what it aims to do is make programming
more similar to natural language (on top of some other technical things that are not relevant right now)

subject verb object

subject.verb(object)

list    . append (item)
subject   verb   object

object oriented code looks more like sentences where subjects (objects) do something (function calls)
to objects (objects)

Object Oriented Code has these postulates

    1) Objects are instances of classes 
    2) classes have their own
        a) data types
        b) member functions
        
We were working with what is called imperative programming before. What OOP does is abstract away
a lot of the scoping issues into things that make more sense

Class: A template to create objects that has member variables and member functions
    1) member variables are commonly called attributes
    2) member functions are commonly called methods
    
A class has its own attributes and methods

Object: An instance of a class
    1) An instance is a version of the class being implemented
        "number" is a class and "1" is an instance of the "number" class
        "animal" is a class and "dog" is an isntance of the "animal" class
        
So you'll hear the phrase "Everything in python is an object" commonly.

How do we make a class: 

There is a class keyword in python that tells python that you're about to make a class
"""

class dog:
    #Created Dog Class
    
    """
        We need to create a special function called the "constructor" which creates instances of objects.
        To create the constructor we need to use a reserved namespace function __init__ for initialize
        
    """
    
    def __init__(self,breed,age,color,name): #Our parameters are self and the attributes that want to specify
        self.breed = breed
        self.age = age
        self.color = color
        self.name = name
        #The body is assigning the parameters to the attributes
        
    def bark(self):
        print(f"{self.name} barks")
        

jerry = dog("Shiba",6,"White","jerry")
print(f"Jerry's age is: {jerry.age}")

""" 
    In this example, jerry is an instance of a dog with attributes
    
    breed = "shiba"
    age = 6
    color = "White"
    
    So we've made a class, we want to create methods for this class. Jerry wants to do stuff
"""

jerry.bark()

"""
Overall you can think of OOP as a way to conveniently store information all under one variable name (class) 
and also create functions that manipulate data about said object
"""

""" 
Lab 5 was a student directory and it was pretty miserable because you had to do a lot of work with manipulating
dictionaries (and especially nested dictionaries) We can make this a lot easier by doing an object oriented
approach
"""

class student:
    #Constructor
    def __init__(self,gradelevel,email,grades,name):
        self.name = name
        self.gradelevel = gradelevel
        self.email = email
        self.grades = grades
        
    #str function for use with print()
    def __str__(self):
        return(f"{self.name}'s name is {self.name}\n {self.name}'s grade level is {self.gradelevel} \n {self.name}'s email is {self.email}\n {self.name}'s grades are {self.grades}")    
            
        
    #Member functions
    
    def updateGrades(self):
        for course in self.grades:
            newgrade = int(input(f"Update Grade for {course}: "))
            self.grades[course] = newgrade
            

mystudent = student(12,"basmacij@calverthall.com",{"math":90,"english":100,"history":85}, "Jack Basmaci")

#mystudent.updateGrades()
print(mystudent.grades)

""" 
So now our student class has a member function (method) that updates the grades of each course the student
takes.
"""

print(mystudent) 

"""
printing an instance of an object does not print out the attributes. Typically we want to print out the 
attributes when we call print(object) 
"""


""" 
So overall python allows for Object Oriented Programming which allows us to create classes and objects
that have attributes (member variables) and methods (member functions) that allow for an easy

subject.verb(object) style of programming. 
"""