import re

def camel_to_snake(camel_str):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()

camel_case_string = "ConvertThisCamelCase"
snake_case_string = camel_to_snake(camel_case_string)

print("Camel case:", camel_case_string)
print("Snake case:", snake_case_string)
