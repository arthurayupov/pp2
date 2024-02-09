def is_pal(input_string):
    cleaned_str = ''.join(input_string.lower().split())
    return cleaned_str == cleaned_str[::-1]

word = str(input())
if is_pal(word):
    print("Word is polindrom")
else:
    print("Word is not polindrom")