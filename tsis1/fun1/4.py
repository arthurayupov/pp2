def filter_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def Prime_list(numbers):
    prime_numbers = [number for number in numbers if filter_prime(number)]
    return prime_numbers

num_list = [1, 2, 15, 9, 13, 100, 11, 19, 23, 31]
res = Prime_list(num_list)
print(res)