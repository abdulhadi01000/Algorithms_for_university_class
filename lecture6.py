def factorial(n:int)->int:
    _factorial = 1
    for i in range(1,n+1):
        _factorial *= i
    return _factorial

def factorial_recursive(n:int)->int:
    if (n <=1):
        return 1
    
    return factorial_recursive(n-1)*n

def NumberToPowerN(base:int,power:int)->int:
    result:int = 1
    for i in range(1,power+1):
        result *= base

    return result

def NumberToPowerN_recursive(base:int,power:int)->int:
    if power == 1:
        return base

    return NumberToPowerN_recursive(base,power-1)*base

def test_functions()->str:
    print("lecture 6 methods: ")
    print(factorial_recursive(5))
    print(factorial(5))
    print(NumberToPowerN(3,3))
    print(NumberToPowerN_recursive(3,3))
    return ""

if (__name__ == "__main__"):
    test_functions()
