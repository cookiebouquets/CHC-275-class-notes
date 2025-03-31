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

Recursion accomplishes two things typically

    1) It typically uses less memory (I'll do an example of this) <= Function calls also stuff on the stack
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
    #Base Case
    if len(word) == 1:
        return True
    
    #Reecursive Case
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

""" 
Our base case is not immediately obvious but there are some natural choices

    Base Case:
    If we're at the end (len(BOARD)-1, len(BOARD[0]) -1), append that to the path
    return true
    
    Recursive Case: 
    We need to check if the move is valid
    
    Three cases:
        1. Recursively path find down (x+1,y)
            a. append if it works
            b. return true
        2. Recursively path find to the right (x,y+1)
            a. append if it works
            b. return true
        3. If we need to back track, just remove the last element of our path 
        
    Return false if we cant find a path 
"""


BOARD = [ 
             [0,1,1,1,0,0,0],
             [0,1,0,1,1,0,0],
             [0,0,0,0,0,1,0],
             [0,0,1,1,0,0,1],
             [0,1,0,0,1,0,1],
             [0,1,0,0,1,0,0],        
    ]
def validmove(board,x,y):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0


def pathfind(board,x,y,path): 
    #Base Case
    if x == len(board) - 1 and y == len(board[0]) -1:
        path.append((x,y))
        return True

    #Recursive 
    if validmove(board,x,y):
        path.append((x,y))
        
        #Down Case:
        if pathfind(board,x+1,y,path):
            return True
        
        #Right Case: 
        if pathfind(board,x,y+1,path):
            return True

        #Backtrack case:
        path.pop() 
    return False
    
def search(board):
    path = []
    if pathfind(board,0,0,path):
        return path
    else:
        return "Path not found"
    
print("Path")
print(search(BOARD))

""" 
Basically anything that you've done with a forloop or while can be done recursively, but it'll be more 
difficult if the problem doesn't really call for it. Path finding is really the best use case of it

And also counting algorithms are very good:

I'm going to a give of string of a's and b's and we want to return a list that counts all of the individual
a's and b's in that string
"""

def iter_as_bs(string):
    count = [0,0]
    for char in string:
        if char == "a":
            count[0] +=1 
        if char == "b":
            count[1] +=1
            
    return count

print("a's and b's")
message = "abbbaabbaab"
print(iter_as_bs(message))

""" 
The algorithm for this is going to be effectively the same thing as doing palindrome. All we want to look at
is the fist letter of the string and recursively call the function on the substring with the first character 
removed

"abbbaabbaab"
 ^ a
 
"bbbaabbaab"
 ^ b
 
"bbaabbaab"
.
.
.
""
^ return the list 

Basecase: is if the string is empty
    1) return the original list
    
Recursive Case:
    return as and bs(list, string-1)
"""

def recursive_as_bs(string,count):
    #Base Case
    if len(string) == 0:
        return count
    
    #Recursive Case
    if string[0] == "a":
        count[0] +=1 
        return recursive_as_bs(string[1:], count)
    if string[0] == "b":
        count[1] +=1 
        return recursive_as_bs(string[1:], count)
    
print("Recursive a's b's")
print(recursive_as_bs(message,[0,0]))

""" 
For people who are interested, a good problem to try is to take a bunch of open and closed parentheses

(())))(()(()(()())())))))())) 

^Recurrsively count each pair of parentheses

base case:
    would be the same thing
    
recursive case:
    you gotta figure that out
"""

""" 
Lab 8: Labrynth 

You have two agents path finding 

    1) player agent: they spawn top left and need to pathfind to the bottom right
    
    2) minotaur agent: they spawn in the middle of the grid and they want to path find to the player agent
    
    coding a reasonable ai for the minotaur is going to be basically impossible in this class, what we're
    going to do is make it path in a random direction up until it hits the player or a wall
    
    if the player exits, they win and if the minotaur finds the player, the minotaur wins
    
    This is most likely going to be the last lab of the year before projects because it's going to be 
    really hard to do. 
    
    It'll be released for both sections day 6
"""
    
#March 31, DAY 6

""" 
I still want to do more recursion, so today we're going to discuss some searching and sorting
algorithms and how it ties into the previous three days of the cycle.

Three main problem types:
    1) Searching a list
    2) Sorting a list
    3) Pathfinding on a graph 
    
We also have Big-O notation to determine the runtime of our algorithms 
"""

nums = [x for x in range(1,100)]

""" 
We're going to assume a sorted list of numbers:

    1)At what index is the number we're looking for 
    
In this case we happened to have all numbers between 1-99 so we can just do a direct lookup, but 
we might not have every number

    2) We don't really know what numbers are in the list 
    
    3) We want to optimize for time complexity 
    
The naive way to do this is to just do a for-loop over the list and return the index where we found 
the number, then we have our result
"""

def linear_search(list,target):
    index = 0
    while index < len(list):
        if list[index] == target:
            return index
        else:
            index+=1
            
            
    if index == len(list) - 1:
        return "Not found"
    
print("Linear search")
print(linear_search(nums,84))

""" 
84 was our target and it was found at the 83rd index because lists start at index 0. So the question is 
how many times did we a check in this algorithm? 

The answer: 84 checks 

Why do we call this algorithm linear search? 

f(x) = x <= linear function

This is called linear search because it just returns the index of the original number, we had to search
every single value in our list up until we found it. 

This algorithm is O(n). 

We can definitely do better than this.
"""

"""  
Has anyone heard of binary search? What binary search does is check the midpoint of our list, and checks
to see if our target is bigger or smaller than the midpoint

bigger or smaller part <= binary part 

    1)If its bigger, look at the middle of the list starting from the original mid point to the end
    2) if its smaller, look at the middle of the list starting from the beginning up until the original 
    midpoint

There is something recursive going on in binary search:

    1) we are looking at increasingly smaller lists up until we get the result or the number isnt in the list
    
This is faster than linear search because we're halving the size of the list after every iteration. 
We're only checking at most half of the amount of numbers from original 


Base Case:
    1) If the midpoint of our list is the actual target 
        return 1
        
    2) If the value isnt in the list
        return not found 
        

Recursive case
    1) Take the midpoint of the list
    2) compare our number to see if its bigger or smaller
        a) If it's bigger, discard the left half of the list
        b) If it's smaller, discard the right half of the list
    3) Do binary search again on the smaller list
    
"""

def binary_search(list,target):
    print(list)
    #BASE CASE: Not Found
    if len(list) == 1 and list[0] != target:
        return "not found"
    
    #BASE CASE: Found at midpoint
    if list[len(list)//2] == target:
        return "found"
    
    #Recursive Case: Bigger, discard right half 
    if list[len(list)//2] > target:
        return binary_search(list[0:len(list)//2],target)
    
    #Recursive Case: Bigger, discard right half 
    if list[len(list)//2] < target:
        return binary_search(list[len(list)//2:],target)
    
print(binary_search(nums,84))

""" 
We found 84 in 4 iterations. Clearly binary search is significantly better than linear search. 

What is the runtime complexity of binary search. 

we are taking a list of numbers and effectively halving at every iteration.

It's O(log n) which is faster than O(n)

This is because halving the size of a list is comparable to logarithmic decay. 

There is a better way to write binary search so that it actually returns the amount of iterations it takes

"""


""" 
We want to sort numbers now. Our postulates are

1) we have a list of unsorted numbers (or sorted)
2) we want to sort them in the least amount of time (optimizing for time complexity).

Let's think of a recursive algorithm to do this.

We know recursion can take a problem and make into smaller subproblems. We want to the same thing for
sorting. 

What if we took a list of numbers and split down the middle and sorted each sublist, then we'll have
a recursive type problem.  

Base Case:
    1) Our list is of length 1 or 0, we're already sorted
    
Recursive Case:
    1) Split our list down the middle
    2) Do the same base case for the two sublists 
    
At the end:
    1) Zip the lists back together
    
This algorithm is called merge sort. It's called merge sort because we're merging two smaller lists
back into a larger list
"""

nums = [7,4,5,9,10,15,13,12,1,3,2]

def merge_sort(nums):
    print(f"merge sort on {nums}")
    
    
    #Base Case: If the list of numbers is length 1 or 0, just return the numbers
    if len(nums) == 1 or len(nums) == 0:
        return nums
    
    
    #Split the list between left and right
    left = merge_sort(nums[:len(nums)//2])
    
    right = merge_sort(nums[len(nums)//2:])
    
    #Zip the lists back together
    ileft = 0
    iright = 0
    
    sorted = []
    
    """ 
    If you don't know how to zip things together, what we have to is compare each element at index 0
    append the smaller one into the sorted list and increment that index by 1 up until we run out of numbers
    """
    
    while len(sorted) < len(nums):
        if left[ileft] < right[iright]:
            sorted.append(left[ileft])
            ileft +=1
        
        else:
            sorted.append(right[iright])
            iright+=1
            
        if ileft == len(left):
            sorted.extend(right[iright:])
            print("Merge Sort Complete")
            return sorted
            
        if iright == len(right):
            sorted.extend(left[ileft:])
            print("Merge Sort Complete")
            return sorted
            
print(merge_sort(nums))
""" 
Merge Sort is O(n log n)
"""