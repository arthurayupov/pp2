import re

p = re.compile(r'[a-z]+_[a-z]+')
s = "hello_world"
match = p.fullmatch(s)

if match:
    print("Match found!")
else:
    print("No match")