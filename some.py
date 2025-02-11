def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False
    
    # Check for divisibility from 2 to square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_number(n):
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        if n % 2 == 0:
            print(f"{n} is not prime and is even.")
        else:
            print(f"{n} is not prime and is odd.")

# Example usage
number = int(input("Enter a number to check: "))
check_number(number)