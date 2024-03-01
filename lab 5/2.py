import re

p = re.compile(r'ab{2,3}')
s = "abb"
match = p.fullmatch(s)

if match:
    print("Match found!")
else:
    print("No match")