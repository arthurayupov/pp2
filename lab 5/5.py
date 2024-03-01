import re

p = re.compile(r'[ ,.]')
s = "This is a test, string. With spaces."
result = p.sub(':', s)

print("Original string:", s)
print("Modified string:", result)
