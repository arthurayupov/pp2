import re

p = re.compile(r'[A-Z][a-z]*')
s = "SplitThisString"
result = p.findall(s)

print("Original string:", s)
print("Splitted string:", result)