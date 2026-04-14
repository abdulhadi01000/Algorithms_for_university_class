def GCD(m:int,n:int)->int:
    t = 0
    while True:
        t = m%n
        if (t == 0):
            return n
        m = n
        n = t

def isPrime(n:int)->bool:
    if ((n <= 1) or (n % 2 == 0)): return False

    if (n == 2): return True

    for i in range(3,n):
        if (n%i==0):
            return False

    return True

def test_functions():
    print("test lecture 2 functions:")
    print(f"GCD(10,100): {GCD(10,100)}")
    print(f"isPrime(123456789): {isPrime(123456789)}")

    return ""
    

if __name__ == "--main--":
    test_functions()