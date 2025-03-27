""" 
This unit will focus on theoretical aspects of computer science:

    1) Asymptotic Analysis
    2) On the practical side: Recursion
    
If you are moving onto 277, this is a preview of concepts you will be working with 
in that class.
"""

""" 
We want a way to quantify how fast our programs run. we do this with a technique
called asymptotic anaylsis 

You can break down a program into two things

    1) The input (size)
    2) The runtime
    
We want to quantify the run time based on the input size

Things that can have sizes:

    1) lists
    2) dictionaries
    3) strings
    
We're also going to use an arbitrary time unit: 

    1) Execution
    
the reason why we use an arbitrary time unit is because the computational power of 
your computer greatly determines how fast something runs

"""

""" 
There's really three buckets of runtimes that matter

    1) Things that are internet ready: Usually in like a second or less
        - Sorting a list
    2) Weather Prediction: Usually in a week or month  
        - Weather prediction
    3) Totally unrunnable: Things that would take multiple lifetimes to run
        - Factoring very large numbers into prime numbers 
        
        
"""

""" 
The main tool of Asymptotic Analysis is something called Big-O. What it does 
is quantifies the runtime in the average case based on the algorithm that we wrote

One more postulate:

running one line of code = 1 execution

We want to characterize programs by functions that take in n-elements and takes however
many executions 

The easiest way to think about this is by an example
"""


def myfunction(list):
    print("function 1")
    #Our list has a size associated with it, we're call it n
    for i in range(len(list)):
        print(i)
    

"""
List = [a,b,c] 
n = 3
output = 3 executions


list = [a,b,c,d]
n = 4
output = 4 executions

list = [a,b,c,d,e]
n = 5
output = 5 executions

if our list was length n, the output is also n executions

the input size and amount of executions is exactly the same. We say this function

is O(n) 
"""

#myfunction([1,2,3,4,5])
#This function is O(n)

"""
The next example is when we "multiply" two loops together
 
"""

def myfunction2(list):
    print("function 2")
    for i in range(len(list)):
        for j in range(len(list)):
            print(i + j)


""" 
Input size is N

Example [1,2,3]
n = 3
range is going to be [0,1,2]

first i-loop:
    first j-loop:
        print
    second j-loop:
        print
    third j-loop:
        print

second i-loop:
    first j-loop:
        print
    second j-loop:
        print
    third j-loop:
        print
        
third i-loop:
    first j-loop:
        print
    second j-loop:
        print
    third j-loop:
        print
        
We have 9 print statements.

3^2 = 9. If we had 4^2 = 16 

"""

#myfunction2([1,2,3,4])
#For our n=3 case, we had 9 executions, for our n=4 case, we had 16 executions
#O(n^2) is the average runtime of this function
#O(n * n = n^2)

""" 
A good time to stop and ask, which is more preferable

O(n) or O(n^2)

The function that blows up slower is typically better.

Other types of common runtimes

O(1)
O(n)
O(n^2)
O(log n)
O(n log n)

Sorted least to great

O(1) - Constant time
O(Log n) - Logarithmic Growth
O(n) - linear time
O(n log n) - linear * logarithmic
O(n^2) - quadratic (typically bad)


"""

def myfunction3(list):
    print("function 3")
    for i in range(int(len(list)**1/2)):
        for j in  range(int(len(list)**1/2)):
            print(i + j)

""" 
From our previous example O(n^2), we had two nested loops so it was really

O(n * n) = O(n^2)

O(sqrt(n) * sqrt(n)) = O(n)
"""

#myfunction3([1,2,3,4])
#This is O(n)

def myfunction4(list):
    #We want to analyze this
    print("function 4")
    for i in range(len(list)):
        for j in range(len(list)):
            print(i + j)

    for i in range(len(list)):
       print(i)
       
"""
Input size of N
Intuitively we have a nested for loop and then we're "adding" another for loop on top

O(n*n + n = n^2 + n)

But really the biggest power wins

O(n^2)

So even though this was technically a O(n^2+n), we classify it as O(n^2)

"""

"""
The last thing I'll show is called constant time:

An algorithm is said to be constant time if it doesn't dependent depend on the input
size at all

"""

def myfunction5(list):
    #Does this function depend on the length of list?
    print("function 5")
    print(1)
    print(2)
    print(3)
    
#myfunction5([1])
#myfunction5([1,2])
#myfunction5([1,2,3])

"""
We would say myfunction5() is a algorithm with constant time.

Constant time is O(1). Technically this is O(3), but you'll literally never see
anyone call constant time anything but O(1).

Analyzing algorithms gets pretty hard when there are base cases <= 277. 
"""

#MARCH 27, DAY 4
"""
Recursion

Vocab Review:

def <function name>(): <== function header

<function name>() <== function call 


Recursion is essentially just functions that call themselves.

This implies that at some point in your function body

def <function name>():
    <function name>()
    
There are some technical considerations at play:

    1) Base Case
    2) Recursive Case
    
We want some way to escape a recursive function without it running essentially forever
"""


def hello():
    print("Hello")
    #Recursive Case
    hello()
    
#hello()
"""
We need a base case in order to make sure our function eventually exits and passes control back python

Not having a base case or a way to have your function end is called a stack overflow <= i'll explain this eventually


""" 

""" 
What are good examples of base cases? We'll do an example

We are a function that does a countdown from n to 0. n is going to be our parameter and we want to make sure
at n = 0, the function stops calling itself

just have an if statement that checks if n = 0 then exit the function (typically a return or something)
"""

def countdown(n):
    #Base Case
    if n == 0:
        return 0 #Return exits a function and returns control back to python
    
    #Recursive case
    print(f"T = {n}")
    countdown(n-1)
    
countdown(10) #This is our most basic example of recursion

""" 
We need:
    1) Base case that guarantees the function ends
    2) Recurisve case that eventually hits the base case 
    
What examples of recursion occur naturally? 

5! = 5 * 4 *3 *2 * 1 <= this kinda looks recursive

What's the base case here:

0! = 1 <= base case

What the general formula is for the factorial

x! = x * (x-1) * (x-2) * ... * 0! <= you can condense this expression into 

x! = x * (x-1)! <= this stores all of the succeeding values in the factorial implicitly

Base Case: 
0! = 1

Recursive Case: 
x! = x * (x-1)! 
"""

def factorial(n):
    #Base Case
    if n == 0:
        return 1
    
    #Recursive Case
    n = n * factorial(n-1)
    return n 

#Factorial of 5=120
print("Factorial")
print(factorial(5))

""" 
Recursion is kinda something that you need to practice over and over again. We should do another example

fibonacci sequence: is a formula that computes a sequence of numbers based on this formula

fib(n) = fib(n-1) * fib(n-2) <= immediately this looks recursive by definition, there's fib on both sides of =

We need the base cases
fib(0) = 1
fib(1) = 1 

"""

def fib(n):
    #Base Case
    if n in [0,1]:
        return 1
    
    #Recursive Case 
    n = fib(n-1) + fib(n-2)
    return n

"""
fib(2) = fib(2-1) + fib(2-2)
       = fib(1) + fib(0) 
       = 1 + 1 = 2

fib(3) = fib(3-1) + fib(3-2)
       = fib(2) + fib(1)
       = 2 + 1 = 3

fib(4) = fib(4-1) + fib(4-2)
       = fib(3) + fib(2)
       = 3 + 2 = 5
"""
print("fib")
print(fib(4))

""" 
So the actual question you should be asking now is why is this useful at all? 

Recursion accomplishes two things typicall

    1) It typically uses less memory (I'll do an example of this)
    2) It's really good at path finding algorithms (basically all of computer science)
    
Most problems in CS boil down to

    1) Doing a lot of math
    2) Sorting some list
    3) Searching some list
    4) path finding 
    
Recursion is good at doing a lot of these things when optimizing for time and space complexity. The 
easiest use case I can come up with immediately is palindrome

palindrome (same word forward and backwards):
    1) Input our word
    2) copied into another variable but backwards
    3) Then check to see if each letter of both the original and copy match up with each other
    
This algorithm is good but it has a huge space problem: we are basically doubling the space requirement by 
having to copy the string into another variable but backwards


"""

def palindrome(word):
    rev = ""
    for char in word:
        rev = char + rev
        
    if word == rev:
        return True
    else:
        return False
    
#We had to double our space requirement and  perform a O(2n) algorithm. We can do better with recursion


""" 
racecar <= we know that this is a palindrome. We want to check it recursively by looking at the ends of 
the string and then each subsequent substring

racecar
r     r
 a   a
  c c
   e
   
We can do this with exactly one string (list). and since Strings pass by reference, we aren't actually making
a new string every time we go down the stack

Base case: 
If we get to the middle of the word, return true

recursive case:
Check the ends
"""

def recursive_palindrome(word):
    if len(word) == 1:
        return True
    
    if word[0] == word[len(word) -1]:
        return recursive_palindrome(word[1:len(word) -1])
    else:
        return False
    
print("palindrome")
print(palindrome("racecar"))
print(recursive_palindrome("racecar"))

"""
Analysis of recursive palindrome: 

Space complexity:

1) A list passes by reference so in the recurisve case we're still pointing to the same place in memory
We're using the same space as the input effectively <- very efficient in this regard

Time complexity:

1) Should be faster than o(n) but it could also just be that 

This is a good example of when recursion could be better than iteration.

The other use case that I mentioned was path finding. 
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
Postulates for path finding: 

    1) We have an entrance and exit (Top left to bottom right)
    2) 1's are walls
    3) 0's are spaces we can cross 
    
Our goal is to write an algorithm recursively that returns a list of all of the coordinates that lead
to a valid path to the exit. <= This is like trying to find a route from your house to school (GPS)

Also we're going to do it with 

    1) No considerations for time or space complexity (This is too hard for this class right now)
    2) Only valid moves are Down and to the Right 
    
We can implement this in 3 functions

    1) Check for a valid move <= helper function
    2) Path find <= this will find a path
    3) search <= will return the path found by path find
"""
def validmove(board,x,y):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0

""" 
Base Case: 
If we're at the exit just return the coordinate that we're at (len(board),len(board[0]))

Recursive Cases:
Down:
    Check if (x+1,y) is a valid move, if it is path find to (x+1,y)
    
Right: 
    Check if (x,y+1) is a valid move, if it is, path find to (x,y+1)
    
    
path find = append to path and go to the next unit (return true)
"""

def pathfind(board,x,y,path): 
    #Base Case
    if x == len(board) -1 and y == len(board[0]) - 1:
        return path
    
    #Recursive Case
    
    if validmove(board,x,y):
        path.append((x,y))
        if pathfind(board,x+1,y):
            return True
        
        if pathfind(board,x,y+1):
            return True
        
        path.pop()
        
    return False
