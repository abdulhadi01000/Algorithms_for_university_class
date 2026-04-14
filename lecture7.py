def to_binary_string(n: int) -> str:
    if n == 0:
        return "0"
    
    bits = []
    temp_n = abs(n)
    
    while temp_n > 0:
        bits.append(str(temp_n % 2))
        temp_n //= 2
        
    binary_str = "".join(reversed(bits))
    
    return f"-{binary_str}" if n < 0 else binary_str


def NumberToPowerN_recursive_logN(base:int,power:int)->int:
    if power == 0:
        return 1
    if power == 1:
        return base

    half_power = NumberToPowerN_recursive_logN(base,power // 2)

    if (power % 2 == 0):
        return half_power*half_power
    else:
        return half_power*half_power*base


def test_functions()->str:
    print("lecture 7 methods: ")
    print(to_binary_string(16))
    print(NumberToPowerN_recursive_logN(10,2))
    return ""

from math import sqrt
if (__name__ == "__main__"):
    test_functions()

