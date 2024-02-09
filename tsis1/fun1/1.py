def change(grams):
    ounces = 28.3495231 * grams
    return ounces

gram = float(input())
result = change(gram)
print(result)