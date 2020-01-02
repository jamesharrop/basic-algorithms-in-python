''' Exercise 11 (and Solution)
Ask the user for a number and determine whether the number is prime or not.
'''

num = int(input("Enter a number: "))

def find_divisors(num):
    divisors = [x for x in range(1, int(num/2)+1) if num%x == 0]
    divisors.append(num)
    return divisors

def is_prime(num):
    return len(find_divisors(num)) == 2

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

def is_prime_faster(num): # It stops looking once it finds any factor
    value = 1
    while True:
        value += 1
        if num % value == 0:
            return(False)
        if value == int(num/2)+1:
            return(True)

print("Try another method:")

if is_prime_faster(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")