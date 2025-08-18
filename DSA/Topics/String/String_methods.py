"""
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values from a dictionary in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Converts the elements of an iterable into a string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning

"""

s = "hello world"
print(s.capitalize())     # Hello world
print(s.casefold())       # hello world
print(s.center(20, '*'))  # *****hello world*****
print(s.count("l"))       # 3
print(s.encode())         # b'hello world'
print(s.endswith("world"))# True
print("h\te\tl\tl\to".expandtabs(4)) # h   e   l   l   o
print(s.find("world"))    # 6
print("My name is {}".format("Ibrahim")) # My name is Ibrahim
print("My name is {name}".format_map({"name": "Ibrahim"})) # My name is Ibrahim
print(s.index("world"))   # 6
print("abc123".isalnum()) # True
print("abc".isalpha())    # True
print("abc".isascii())    # True
print("123".isdecimal())  # True
print("123".isdigit())    # True
print("var1".isidentifier()) # True
print("hello".islower())  # True
print("12345".isnumeric())# True
print("hello!".isprintable()) # True
print("   ".isspace())    # True
print("Hello World".istitle()) # True
print("HELLO".isupper())  # True
print("-".join(["a", "b", "c"])) # a-b-c
print("hi".ljust(10, "*"))  # hi********
print("HELLO".lower())    # hello
print("   hello".lstrip()) # 'hello'
trans = str.maketrans("h", "H")
print("hello".translate(trans)) # Hello
print("apple pie".partition(" ")) # ('apple', ' ', 'pie')
print("hello world".replace("world", "Python")) # hello Python
print("banana".rfind("a")) # 5
print("banana".rindex("a")) # 5
print("hi".rjust(10, "*")) # ********hi
print("apple pie".rpartition(" ")) # ('apple', ' ', 'pie')
print("a,b,c".rsplit(",")) # ['a', 'b', 'c']
print("hello   ".rstrip()) # 'hello'
print("a b c".split()) # ['a', 'b', 'c']
print("line1\nline2".splitlines()) # ['line1', 'line2']
print("hello".startswith("he")) # True
print("   hello   ".strip()) # 'hello'
print("HeLLo".swapcase()) # hEllO
print("hello world".title()) # Hello World
print("hello".upper()) # HELLO
print("42".zfill(5)) # 00042
