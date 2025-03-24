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