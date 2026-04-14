def sum_of_squares(n:int)->int:
    s = 0
    if n <= 0:return 0

    for i in range(n):
        s+= i*i

    return s

def test_functions()->str:
    print("lecture 5 methods: ")
    print(f"sum_of_squares: {sum_of_squares(9)}")

    return ""

if (__name__ == "__main__"):
    test_functions()