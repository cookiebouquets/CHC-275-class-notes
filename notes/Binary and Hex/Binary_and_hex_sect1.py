""" 
    Today we're going to cover Binary and Hex Number systems, chr() and ord()
    
    Lab 7 will be about manipulating strings through manipulating them as ASCII characters and their values 
"""

""" 
    First things first: We know computers work in 0s and 1s. This is called binary. 
    
    Historically why do we only use 0s and 1s. This is a result of electrical engineering back in the 
    1940s. When computers were initially being made they were basically large rooms of vacuum tubes and 
    you typically need n-1 electrical components to distinguish between n voltage levels.
    
    to distinguish between a high and low voltage, we need exactly 1 measuring device. That's why we use
    binary today, because electrical engineering back then sucked really bad. 
    
    1 = high voltage/on/true
    0 = low or no voltage/off/false
    
    This makes sense to us.
    
    Binary numbers only have 2 digits 0 and 1
    Decimal Numbers which we are most familiar with have 10 digits
    0,1,2,3,4,5,6,7,8,9 <= 10 digits 1-9 including 0 
    
    We want to encode our decimal numbers in binary.
    
    In decimal numbers, every "place" is a power of 10
    
    5492
    
    5000 = 5 *10^3 
    400 = 4*10^2
    90 = 9*10^1
    2 = 2*10^0 
    
    5492 = (5 *10^3) + (4*10^2) + (9*10^1) + (2*10^0)
    
    if this is base 10,
    
    what do you think binary is? 
    
    Base 2, so each place is a power of 2.
    
    1   0   1   1
    2^3 2^2 2^1 2^0
    
    2^3 + 2^1 + 2^0 = 11
    
    11 in binary is 1011
    
    Our algorithm for switching from decimal to binary is 
    
    1) take our number and divide by 2 
    2) if the remainder is 1, make that place 1
    3) if the remainder is 0, make that place 0
    
    11 % 2 = 5 remainder 1 
    5 % 2 = 2 remainder 1
    2 % 2 = 1 remainder 0
    1 % 2 = 0 remainder 1
    
    4) Take the result and replace the digits in ascending order (down then back up)
    
    1011 = 11 which is what we expected
    
    one 1 or 0 is called a bit. This is a miserable form of measurement. We only care about collections of bits
    
    1 bit = one 1 or 0
    1 byte = 8 bits 
    kilobyte = 1024 bytes
    megabyte = 1024 kilobyte
    .
    .
    .
    1 byte = 0000 0000 
    
    one byte is two registers of 4 bits. What is the biggest number you can store in a byte? 
    
    2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5 +2^6 + 2^7
"""

byte = 2**0 + 2**1 + 2**2 + 2**3 + 2**4 + 2**5 +2**6 + 2**7
#print(byte)

"""
    The biggest number you can store in a byte is 255.
    
    0000 < what is the biggest number you can store in a 4 bit register?
    
    15 
    
    1101 1010 1011 1101 0101 1100 0011 0001 1011 0010 0100 
    
    Is there a better way to write binary numbers in shorthand?
    
    Hexadecimal numbers = Base 16
    
    We have a problem: 
    
    we have only have 10 digits to work with 0-9 So we need to find more characters to represent numbers
    10-15
    
    we should leters for 10-15
    
    
    0 0         7 7         14 e 
    1 1         8 8         15 f
    2 2         9 9 
    3 3         10 a
    4 4         11 b
    5 5         12 c    
    6 6         13 d 
    
    four bit registers can actually be represented as 1 hex number 
    
    1101 <= 13 <= d
    
    1101 1010 1011 1101 0101 1100
    
    dabd5c
    
    0000 0000 0000 0000 0000 0000
        R         G         B
        
    RGB color palette all 0s is black
    
    All 1s is White
    
    #FFFFFF is pure white
    
    #FF0000 < Red
    #00FF00 < Green
    #0000FF < Blue
    
    
    So really the individual byte registers correspond to the intensity of Red, Green, Blue
    
    (255,255,255)
    
    This is basically all I have to say for this for now 
    
    Next class ord() and chr() and ASCII
    
    
"""

#DAY 3, MARCH 7

""" 
    Today I'm going to talk about encoding data (ASCII) and how you can in python (ord()) and (chr())
    and also applications of these things (cryptography)
    
    Last class we discussed Binary and Hex Numbers. We also know the largest number we can store in a byte
    is 255. There is an international standard for how characters are represented on computers. 
    
    When you type in a letter, its going to get "encoded" into a number
    
    encoding = assigning numerical values to data that is not inherently numerical.
    
    Strings = not numerical, we can encode this (ASCII)
    
    pictures = not numerical, we can encode this (rgb)
    
    ASCII takes the most common 255 roman-numeric characters and assigns to a number between 1-255.
    
    a = 67 in ASCII
    
    we can do math on things with their ASCII values.
    
    In other programming languages, individual characters of strings have their own primitive data type
    
    chars <= individual character of a string
    
    and what chars have is two pieces associated with them
    
        1) their graphical representation (Letters and stuff)
        2) ASCII numerical value
        
    In python however, wwe don't have char as a datatype. We have two functions that behave pretty much
    identically to chars which are called
    
    chr(<num>) = converts a number to its lexicographic representation
    ord(<char>) = converts a character to its ASCII value
    
    These two functions are basically inverses of each other (for those in precalc/alg 2).
    
    chr() the name is pretty obvious were it comes from, its shorthand for char
    
    ord() is not nearly as obvious, it comes from the word "order" which is a math term for things that
    loop around. 
    
"""


char = "a"

print(ord(char))
#ASCII value of "a" is 97

num = 58
print(chr(num))
#ASCII char of 58 is ":"

""" 
    How is this stuff useful at all in the slightest? 
    
    We all have kinda heard what cryptography is. The use of encoding our non-numerical data into ASCII is 
    to do cryptography pretty effectively 
    
    What cryptography essentially is - the encoding of data in a secure way so that malicious actors cant 
    figure what the message is
    
        plaintext = your message
        key = the key by which you encrypt your message
        ciphertext = your message after encrypting it 
        
    So the question is, how do we make ciphertexts? Let's do an example
    
    plaintext is CHC the easiest way to encrypt this is to use a Shift Cipher
    
    Shift Cipher -> takes all ASCII values and shifts them over by a certain number
    
    plaintext is CHC
    key is +3
    ciphertext is FKF
    
    This is the most basic form of encryption
    
    To decrypt, you would just do -3. 
    
    This example is super easy because there are only 3 letters that we're manipulating. What about large strings
    of text?

    
"""

plaintext = "Here, you can explore your passions to reach your potential and realize your purpose, on our campus and in the world beyond. A Calvert Hall education is a transformative experience that continues long after graduation. Our students become Men of Intellect, Men of Faith, and Men of Integrity, and the relationships they develop over four years at The Hall last forever."
#I want to do a shift cipher on this +3, but there is hundreds of characters in here. How do we automate this in python?
key = 3
converted = []
for char in plaintext:
    encode = ord(char)
    converted.append(encode)
    
#print(converted)
encrypted_nums = []
for num in converted:
    enc = num + key
    encrypted_nums.append(enc)
    
#print(encrypted_nums)
ciphertext =""
for num in encrypted_nums:
    char = chr(num)
    ciphertext = ciphertext + char

print(plaintext)
print(ciphertext)

#Decryption
converted = []
for char in ciphertext:
    converted.append(ord(char))
    
decrypted = ""

for num in converted:
    decrypted = decrypted+ chr(num - key)
    
print(decrypted)

""" 
    This is our Shift Cipher Example.

    In Lab 7, 
    
        -you'll be implementing RSA encryption
    
        -you'll also be manipulating images with RGB values
        
    So other things that are of importance with ASCII values:
    
        -you'll definitely need to remember what % does. 
        
        % is mod 
        
        mod = division by a number and it returns the remainder
        
        15 mod 7 = 1
        
    Many things in cryptography involve the use of % (ESPECIALLY RSA) so you'll need to use it in Lab 7. 
    
    Next Class I'm assigning lab 7
"""

