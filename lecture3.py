def SumAllOddNumbers(my_list:list[int])->float:
    sum_ = 0
    for i in my_list:
        if (i % 2 != 0):
            sum_+=i

    return sum_

def printingAllArrayElements(my_list:list[int]):
    for i in my_list:
        print(f"{i} ",end="");
    print()
    return ""

def FidingMin(my_list:list[int]):
    min_ = my_list[0]
    for i in my_list:
        if (i < min_):
            min_ = i
    return min_

def FidingMax(my_list:list[int]):
    max_ = my_list[0]
    for i in my_list:
        if (i > max_):
            max_ = i
    return max_

def FindingRangeInUnsortedArray(my_list:list[int])->int:
    minimum = FidingMin(my_list)
    maximum = FidingMax(my_list)

    return maximum - minimum

def FindingRangeInSortedArray(my_list:list[int])->int:
    sorted_array = sorted(my_list)#make sure it's sorted
    last_index = len(sorted_array) - 1

    return sorted_array[last_index] - sorted_array[0]

def FindingIfArrayIsSorted(my_list:list[int])->bool:
    for i in range(len(my_list)-1):
        if (my_list[i] > my_list[i+1]):
            return False
    return True


def test_functions()->str:
    print("lecture 3 methods: ")
    numbers:list[int] = [1,2]
    print(f"printingAllArrayElements: ",end="")
    printingAllArrayElements(numbers)

    print(f"SumAllOddNumbers: {SumAllOddNumbers(numbers)}")

    print(f"FindingRangeInUnsortedArray: {FindingRangeInUnsortedArray(numbers)}")
    
    print(f"FindingRangeInSortedArray: {FindingRangeInSortedArray(numbers)}")

    print(f"FindingIfArrayIsSorted: {FindingIfArrayIsSorted(numbers)}")

    return ""

if (__name__ == "__main__"):
    test_functions()