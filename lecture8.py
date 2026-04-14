#this is hard to understand for me
def to_binary_recursive_string(n: int) -> str:
    if n == 0:
        return "0"
    
    temp_n = abs(n)
    def binary_builder(n:int)->str:
        if n == 0:
            return ""

        return binary_builder(n//2) + f"{n%2}"

    
    binary_str = binary_builder(abs(n))

    return f"-{binary_str}" if n < 0 else binary_str

def fibonacci_recursive(n:int)->int:
    if (n == 1 or n == 0):
        return n

    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci(n:int)->int:
    current_val = 0
    next_val = 1

    for i in range(n):
        temp = next_val+current_val
        current_val = next_val
        next_val = temp
    
    return current_val

def power_of_two_recursive(n:int)->int:
    if (n == 0): return 1

    if (n < 0):
        return 1/power_of_two_recursive(n*-1)

    return 2 * power_of_two_recursive(n-1)

def power_of_two_recursive_V2(n:int)->int:
    if n == 0:
        return 1
    if n < 0:
        return 1 / power_of_two_recursive_V2(-n)
    
    half = power_of_two_recursive_V2(n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return 2 * half * half

def power_of_two(n:int)->int:
    result = 1
    for i in range(1,n+1):
        result*=2
    return result

def test_functions()->str:
    print("lecture 8 methods: ")
    print(f"to_binary_recursive_string(16): {to_binary_recursive_string(16)}")
    print(f"fibonacci(9):{fibonacci(19)}")
    print(f"fibonacci_recursive(9):{fibonacci_recursive(19)}")
    print(f"power_of_two(10): {power_of_two(10)}")
    print(f"power_of_two_recursive(10): {power_of_two_recursive(10)}")
    print(f"power_of_two_recursive_V2(10): {power_of_two_recursive_V2(10)}")
    return ""

from math import sqrt
if (__name__ == "__main__"):
    test_functions()

