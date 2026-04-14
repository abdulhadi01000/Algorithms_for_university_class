
def printSquearofStrars(n:int = 1):
    for i in range(n):
        for j in range(n):
            print("*" , end="")
        print()
    return ""

def AddMatrices(
    mat1: list[list[int]],
    mat2: list[list[int]]
    ) -> list[list[int]]:

    result: list[list[int]] = []
    rows= len(mat1)
    cols= len(mat1[0])
    
    for i in range(rows):
        row_result = []
        for j in range(cols):
            row_result.append(mat1[i][j] + mat2[i][j])


        result.append(row_result)

    return result

def MultiMatrices(
    a: list[list[int]],
    b: list[list[int]]
    ) -> list[list[int]]:

    result:list[list[int]] = []
    rows_mat1 = len(a)
    cols_mat1 = len(a[0])
    cols_mat2 = len(b[0])

    for i in range(rows_mat1):
        row_result = []
        for j in range(cols_mat2):
            cell_sum = 0
            for k in range(cols_mat1):
                cell_sum += a[i][k] * b[k][j]
            row_result.append(cell_sum)
        result.append(row_result)

    return result

def IsArrayUniqe(my_list:list[int])->bool:
    array_length = len(my_list)
    
    for i in range(array_length):
        for j in range(i + 1, array_length):
            if (my_list[i] == my_list[j]):
                return False;

    return True;


def test_functions():
    print("test lecture 4 functions:")
    print("printSquearofStrars: ")
    printSquearofStrars(5)
    
    matrix1 = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    
    matrix2 = [[7,8,9],
               [6,5,4],
               [1,2,3]]
    
    added_matrix = AddMatrices(matrix1,matrix2)
    print(f"add_matrices: {added_matrix}")

    multi_matrix = MultiMatrices(matrix1,matrix2)
    print(f"mult_matrix: {multi_matrix}")

    uniqe_array = [1,2,3,4,5]
    un_uniqe_array = [1,2,3,4,5,1]
    print(f"is array {uniqe_array} is uniqe? {IsArrayUniqe(uniqe_array)}")
    print(f"is array {un_uniqe_array} is uniqe? {IsArrayUniqe(un_uniqe_array)}")

    return ""
    

if __name__ == "--main--":
    test_functions()
