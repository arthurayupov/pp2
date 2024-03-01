import re

p = re.compile(r'a.*b$')
s = "aanythingb"
match = p.fullmatch(s)

if match:
    print("Match found!")
else:
    print("No match")
