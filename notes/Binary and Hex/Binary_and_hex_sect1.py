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
print(byte)

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
    
    
    So really the individual byte registers correspond to the intensity of Red,Green,Blue
    
    (255,255,255)
    
    This is basically all I have to say for this for now 
    
    Next class ord() and chr() and ASCII
"""