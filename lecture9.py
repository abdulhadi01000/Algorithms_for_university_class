def sequential_search(val:int,my_list:list[int])->int:
    for i in range(len(my_list)):
        if (my_list[i] == val):
            return i
    
    return -1#not found!

def sequential_search_on_sorted_array(val:int,my_list:list[int])->int:
    sorted_array:list[int] = sorted(my_list)
    for i in range(len(sorted_array)):
        if (sorted_array[i] == val):
            return i
        if (sorted_array[i] > val):
            return -1
    
    return -1#not found!

def selectionSort(my_list:list[int]):
    length = len(my_list)

    for i in range(length):
        min_ = i
        for j in range(i+1,length):
            if (my_list[j] < my_list[min_]):
                min_ = j
        temp = my_list[i]
        my_list[i] = my_list[min_]
        my_list[min_] = temp

    return f"{my_list}"

def test_functions()->str:
    print("lecture 9 methods: ")    
    print(f"sequential_search(10,[1,2,3,4,5,6,7,8,9]): {sequential_search(10,[1,2,3,4,5,6,7,8,9])}")
    print(f"sequential_search(10,[1,2,3,4,5,6,7,8,9,10]): {sequential_search(10,[1,2,3,4,5,6,7,8,9,10])}")
    print(f"sequensal_search_on_sorted_array(10,[1,2,3,4,5,6,7,8,9]): {sequential_search_on_sorted_array(10,[1,2,3,4,5,6,7,8,9])}")
    print(f"sequensal_search_on_sorted_array(10,[1,2,3,4,5,6,7,8,9,10]): {sequential_search_on_sorted_array(10,[1,2,3,4,5,6,7,8,9,10])}")
    your_list = [9,8,7,6,5,4,3,2,1]
    print(f"selectionSort({your_list}): {selectionSort(your_list)}")
    return ""

if (__name__ == "__main__"):
    test_functions()
