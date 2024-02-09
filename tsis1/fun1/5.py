from itertools import permutations

def print_permutations(input_string):
    
    perm_set = set(permutations(input_string))
    
    print(f"All string permutations '{input_string}':")
    for perm in perm_set:
        print(''.join(perm))

user_input = input("Enter the string: ")

print_permutations(user_input)