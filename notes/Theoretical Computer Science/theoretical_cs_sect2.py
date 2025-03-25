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

myfunction([1,2,3,4,5])
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

myfunction2([1,2,3,4])
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

myfunction3([1,2,3,4])
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
    
myfunction5([1])
myfunction5([1,2])
myfunction5([1,2,3])

"""
We would say myfunction5() is a algorithm with constant time.

Constant time is O(1). Technically this is O(3), but you'll literally never see
anyone call constant time anything but O(1).

Analyzing algorithms gets pretty hard when there are base cases <= 277. 
"""