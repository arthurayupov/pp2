import re

p = re.compile(r'(?<=[a-z])([A-Z])')
s = "InsertSpacesInThisString"
result = p.sub(r' \1', s)

print("Original string:", s)
print("Modified string:", result)