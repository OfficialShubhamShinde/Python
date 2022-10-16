"""
Something about Regular Expression:
    1) string mai se spasific character nikalne ke liye easy hota hai.
    2) import re kare for adding regilaer expression.
    3) There are some function in regular expression.
    4) in regular expression we are using raw statement, is for print such kind of character which print statement can not print. For Example: print("/n") is new line character. and raw string written as: print(r"/n")
        a) findall
        b) search
        c) split
        d) sub
        e) finditer
    5) finditer baki ke sare function ka kam krta hai.
"""

"""
Some Meta Character and special sequences: 
    1) [] A set of characters
    2) \ Signals a special sequence (can also be used to escape special characters)
    3) . Any character (except newline character)
    4) ^ Starts with
    5) $ Ends with
    6) * Zero or more occurrences
    7) + One or more occurrences
    8) {} Exactly the specified number of occurrences
    9) | Either or
    10) () Capture and group
    
    Special Sequences:
    12) \A Returns a match if the specified characters are at the beginning of the string
    13) \b Returns a match where the specified characters are at the beginning or at the end of a word r” ain\b.”
    14) \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
    15) \d Returns a match where the string contains digits (numbers from 0-9)
    16) \D Returns a match where the string DOES NOT contain digits
    17) \s Returns a match where the string contains a white space character
    18) \S Returns a match where the string DOES NOT contain a white space character
    19) \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
    20) \W Returns a match where the string DOES NOT contain any word characters.
    21) \Z Returns a match if the specified characters are at the end of the string 

"""
# Syntex:
import re

str = "I am Shubham Shindeeee. My Mo No is +917774882080"
# finditer function:

# for searching in string:
search = re.compile(r'am')
matchesSearch = search.finditer(str)
for match in matchesSearch:
    print(match)

# Any Character (.)
"""Print any character in string"""
anyChar = re.compile(r'.')
# anyChar = re.compile(r'.I am')  # . ke bad I am chaiye wahi print hoga
matchesAnyChar = anyChar.finditer(str)
for match in matchesAnyChar:
    print(match)

# Starts With
"""1) Return kr raha hoga to match object return krega
   2) Starts ho rahi hai to hi karega return match object.
   3) for searching starts with use (^'')"""
startsWith = re.compile(r'^I am')
matchStartsWith = startsWith.finditer(str)
for match in matchStartsWith:
    print(match)

# Ends With
"""1) end mai $ likhe
   2) agar string khatam ho rahi hai de huwi value se to match object return krega.
   3) for searching starts with use ($'')"""
endsWith = re.compile(r'Shinde$')
matchEndsWith = endsWith.finditer(str)
for match in matchEndsWith:
    print(match)

# * (Zero or more occurrences) :
"""1) * jis character ke bad lagaya ho wo character kitne bhi bar
   2) """
star = re.compile(r'de*')
matchStar = star.finditer(str)
for match in matchStar:
    print(match)

# + (One or more occurrences)
"""1) ek to hona chaiye"""
pluse = re.compile(r'de*')
matchPluse = pluse.finditer(str)
for match in matchPluse:
    print(match)

# {} Exactly the specified number of occurrences
"""1) Exactli {} is me likhe gaye value pe wo character ane chaiye"""
exact = re.compile(r'Sh{1}')
matchExact = exact.finditer(str)
for match in matchExact:
    print(match)

# () group
"""1) group chaiye () is me likhe gaye chiz ka. our {} wo kitne bar  """
group = re.compile(r'(xy){1}')
matchGroup = group.finditer(str)
for match in matchGroup:
    print(match)

# | Either or
"""1) ek to ye chaiye wrna ye chaise
   2) do no maise ek milega."""
eitherOr = re.compile(r'de* | Shubham')
matchEitherOr = eitherOr.finditer(str)
for match in matchEitherOr:
    print(match)

# Special Sequences:
# \A
"""1) Wo charcater string ke starting mai he to match return krega"""
backslashA = re.compile(r'\AI am')
matchBackSlashA = backslashA.finditer(str)
for match in matchBackSlashA:
    print(match)

# \b
"""1) string mai kaha bhi wo word chaiye"""
backslashb = re.compile(r'\bShinde')
matchBackSlashb = backslashb.finditer(str)
for match in matchBackSlashb:
    print(match)

# \d
"""1) For digite
   2) digit mai dash hoge fir digit hoge to --->"""
degit = re.compile(r'\d{2}\d{10}')
matchDegit = degit.finditer(str)
for match in matchDegit:
    print(match)