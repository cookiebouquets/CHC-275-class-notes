""" 
     This cycle we will be covering number systems, primarily binary and hex. We will also cover
     
     chr() and ord() in python, and how they can be used to manipulate string data
     
     Lab 7 will be a smattering of problems that involve manipulating data in various number systems. 
"""

""" 
    First thing we need to discuss is why do we care about binary at all? 
    
    Computers read data as 1s and 0s, the reason why this is mostly a historical electrical engineering problem
    
    Back in the 1940s when computers were vacuum tubes, it really only made sense to distinguish between
    high and low voltage because the equipment back then was just straight up bad. So the equipment was larege
    and you typically need n-1 sensing components to distinguish between n different voltage levels
    
    2 states is the easiest thing to distinguish because we only need 1 sensing component, if we wanted 10
    states we would 9, so that would just miserable back then to try and distinguish states in decimal numbers
    
    It also turns out that binary is really efficient way to manipulate data. < we care about this a lot in CS
    
    
    How exactly does binary work? The easiest way to do this is to start with decimal
    
    by decimal i mean base 10. In a base 10 number, each "place" corresponds to a power of 10, base 10
    
    5192 
    
    5*(10^3)+1*(10^2)+9*(10^1)+2*(10^0) <= this expression is equivalent to 5192 
    
    Binary numbers are pretty much the same thing, but we are working in base 2. So everything is in powers
    of 2. 
    
    in base 10, the digits that we have are 0-9, if we had 10 it would be the next place over
    
    in binary (base 2), the digits that we have are 0,1 <= two states that correspond positionally to 
    powers of 2
    
    How do we represent binary numbers? Same deal as decimal numbers, but each "place" can only be 0 or 1
    
    and each place corresponds to a power 2
    
    Let's represent 9 as a binary number 
    
    9 > 8 + 1 
    
    So we can write this as 
    
    1001
    
    The rightmost place is the 2^0 which is just 1 and the fourth position is 2^3 which is 8.  
    
    Some nomenclature: 
    
    Each individual 1 and 0 is called: bit
    
    bits are the smallest piece of information a computer can parse

    Bits are also a completely miserable unit of measurement 
    
    The next unit of measurement we care about is: Byte
    
    How big is a byte: 8 bits
    
    1 bit = 1 or 0
    1 byte = 8 bits
    1 kilobytes = 1024 bytes 
    1 megabyte = 1024 kilobytes
    ...
    
    conversion from decimal to binary: Take our number and mod by 2, if theres a remainder put a 1 if not
    leave it 0
    
    9 % 2 = 4 remainder 1 
    
    1
    
    4 % 2 = 2 remainder 0
    
    10
    
    2 % 2 = 1 remainder 0
    
    100 
    
    1 % 2 = 0 remainder 1
    
    1001 <= 9 which corresponds to the previous answer that we got 
    
    So just a review (for decimal): 
    
 _     _   _     _      _    _
10^5 10^4 10^3  10^2  10^1  10^0

for binary

 _   _   _   _   _   _   _   _ 
2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
    
Each position corresponds to a power of 2

The problem with binary is that this gets miserable incredibly quickly 


1011 1100 1011 1010 1101 0011 <= This is a huge number and is a lot to type out. So we as genius human beings

chose hexadecimal as a way to rewrite binary numbers in small amounts of space

Binary = base 2
Decimal = Base 10
Hexadecimal = Base 16

Base 16 for a reason: Biggest number you can store in 4 bits is 16, so Hex numbers represent binary numbers
in much smaller pieces of information

We have a problem: we only have 10 digits to work with 0-9. So how do we represent base 16 with only 
10 digits? The answer: Start using letters 

0 0         7 7         14 e 
1 1         8 8         15 f
2 2         9 9 
3 3         10 a
4 4         11 b
5 5         12 c    
6 6         13 d


four bits is exactly 16 So we can convert binary numbers into hex numbers by just looking at 
groupings of 4

1011 1100 1011 1010 1101 0011
b      c   b    a     d    3

bcbad3

^This is our hexadecimal number. We took our ginormous number and compressed it down to exactly 6 characters

Converting from binary to hex is really easy,
Converting from hex to binary is also really easy,

Converting from decimal to binary is easy,
Converting from binary to decimal, also easy

Converting from decimal to hex  <= kinda hard to do off the dome. We should write algorithm for this because
manipulating hex numbers is a pain because we're going to be dividng ginormous numbers into each other.

Decimal to hex is easier than hex to decimal because we can just mod 16 and the remainder corresponds to our 
mapping of characters (0-9,a-f). <= i'm going to leave this on the lab.

So we now know that binary numbers are how information is stored on computers. How do we manipulate this 
data in meaningful ways? We can do something called bitwise operations. 

Recall from if statements, we can also augment with (AND) terms and (OR) terms. So them true/false can be
evaluated by the individual truth values of the statements along with our AND and OR operations. We can do
the same thing with our binary numbers. We do what is called bitwise operations and compare binary numbers
term by term

Let's start with AND 

The truth table for and 

1 AND 1 = 1
1 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0

If both things are on, we get 1, if not, we get 0 

We can do the same thing for OR:

1 OR 0 = 1
0 OR 1 = 1
1 OR 1 = 1
0 OR 0 = 0

Using these truth tables, we can construct expressions on large binary numbers

    1011 1101
OR  0101 1010
_____________
    1111 1111

So none of them were both zeros. How about AND

    1011 1101
AND 0101 1010
_____________
    0001 1000
    
Sol we got 0001 1000 from using an AND gate bit by bit on our two numbers. The question is: How exactly
is this useful? 

Most if not all math operations are bitwise operations on binary numbers. (Look up adder/half adder
circuits) 

We can also do cryptography with bitwise operations (You'll see these on CTFs).

chc and encrypt it with the key acd using XOR

So i explain what XOR is. XOR stands for exclusive OR, its basically the same as OR but instead you also
consider the 1 XOR 1 case and set that equal to 0    

XOR Truth Table:

1 OR 0 = 1
0 OR 1 = 1
1 OR 1 = 0
0 OR 0 = 0

We need XOR because OR by itself does not allow you to recover information backwards. OR is not an invertible
function (for those in precalc/algebra 2, etc)

chc and convert it to binary with this scheme

1 a 5 e 9 i
2 b 6 f 10 j
3 c 7 g 11 k
4 d 8 h 12 l
    
We can then convert CHC into a a string of decimal numbers

CHC => 383 => 0011 1000 0011
ACD => 134 => 0001 0011 0100

Now what I can do is XOR CHC by ACD and get an encrypted message out of this

    0011 1000 0011
XOR 0001 0011 0100
__________________
    0010 1011 0111 <= our result after XOR 
    
Convert 0010 1011 0111 back to decimal => 2 11 7 => BKG

encrypting CHC by ACD => BKG as our encrypted text

This kind of encryption is called a one-time pad encryption. Next Class I will show how to decrypt this

Hint: You just need to XOR again by the key.  
    
    
"""

#MAR 4, DAY 6

""" 
    Today we are going to cover two functions in python, ord() and chr() which are pivotal to 
    advanced string manipulation in python.
    
    So last class i covered binary and hex number systems. So there's a thing called ASCII
    
    ASCII - international standard for character representation for computing devices. This means that 
    all computers follow the same protocol for displaying text.
    
    1 byte = 8 bits = 00000000 
    the max number you store in a byte is exactly 255. 
    
    11111111 <= this is 255 
    
    What ASCII does is takes the most common 255 characters in any alphabet and assigns them to a number. 
    
    a = 67
    
    So that means when we type in strings, they are interpreted as binary numbers with equivalencies to
    their ASCII values.
    
    So you know that binary numbers are how computers work, this is then extended to ASCII
    
    In python, we want to manipulate strings both as characters and also numerically. In other languages
    
    like, C, C++, Java, individual characters have their datatype called char, but in python, chars are 
    just one character strings. 
    
    Chars = one character in ascii + their underlying numerical value 
    
    In python we don't have chars, we only have strings. So to work around this there are two python
    functions that go back and forth between numerical ASCII value and individual characters
    
    chr(<num>) = converts num to ASCII character
    chr stands for char
    
    ord(<char>) = converts ASCII character to num 
    ord stands for order which is a math term
    
    Remember that strings in python are also lists. lists of individual characters
"""

message = "Lets go CHC!"
#I want to convert this to its individual ASCII values

converted = []
for char in message:
    converted.append(ord(char))

print(converted)

"""
    Now we have a list called converted and its a list of numbers so no we can do math on these numbers.
    
    Application of this is cryptography. 
    
    One of the most common ciphers (method of encryption) is called the Caesar Cipher. What this does is
    takes all of the ASCII values and shifts them over by a certain number. (shift cipher)
    
    For example, 
    
    CHC + 3 -> FLF <= Encrypted text after a caesar cipher. 
    
    How can automate this? and also this kinda sucks to do by hand.
"""
shifted = []
for num in converted:
    num = num+3
    shifted.append(num)
    
print(shifted)
    
#Now we have shifted ASCII Values, now we can convert them back into our letters using chr()

encrypted = ""
for num in shifted:
    encrypted = encrypted + chr(num)

print(f"Original Message {message}")    
print(f"Encrypted message {encrypted}")


#Now how do we decrypt this? We can do the same process but backwards. If our messahe was shifted +3
#We need to shift it minus three

converted = []
for char in encrypted:
    converted.append(ord(char))
    
    
decrypted = ""    
for num in converted:
    num = num - 3
    decrypted = decrypted + chr(num)
    
print(f"decrypted text: {decrypted}")

""" 
    This is an example of a shift/caesar cipher. In the lab you'll probably have to implement a more
    complicated encryption scheme than this. 
    
    So you can get pretty creative with this stuff 
"""

message = "CHC"
keys = [3,7,45]

converted = []
for char in message:
    converted.append(ord(char))


print(converted)

encrypted = ""
for i in range(len(converted)):
    enc = converted[i] + keys[i]
    enc = chr(enc)
    encrypted = encrypted + enc

        
print(f"Original Message:  {message}")
print(f"Encrypted Message: {encrypted}")
#So now we took our message and encrypted it using a variable list of keys

""" 
    This is much better than the Casear Cipher obviously because of something called frequency analysis
    
    In a message of 30 or more characters, the english alphabet tends to follow a certain distribution. 
    The caesar cipher does not change the distribution, all it does is shift it left or right
    
    So in our new example where we had a different key for each character, this is now not nearly as
    susceptible to a frequency analysis attack on our encrypted message. 
"""
converted = []
for char in encrypted:
    converted.append(ord(char))
    
decrypted = ""
for i in range(len(converted)):
    enc = converted[i] - keys[i]
    enc = chr(enc)
    decrypted = decrypted + enc
    
print(f"Decrypted message {decrypted}")

""" 
    This is basically all I have planned for this class. The lab is going to be stuff on binary/hex
    
    and then also cryptography/string manipulation using ord() and chr() 
"""