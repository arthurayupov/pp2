import re

p = re.compile(r'ab*')
s = "abbb"
match = p.fullmatch(s)

if match:
    print("Match found!")
else:
    print("No match")