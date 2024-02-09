def solve(numheads, numlegs):
    for x in range(numheads + 1):  # Corrected variable name from 'i' to 'x'
        y = numheads - x  # Corrected 'y = numheads - 1' to 'y = numheads - x'
        if 2 * x + 4 * y == numlegs:
            return x, y  # Return both x and y instead of numlegs
    return None

x = int(input("Enter number of chicken heads: "))
y = int(input("Enter number of cow heads: "))
res = solve(x, y)
if res:
    chicken_heads, cow_heads = res
    print(f"Number of chicken heads: {chicken_heads}, Number of cow heads: {cow_heads}")
else:
    print("No solution found.")