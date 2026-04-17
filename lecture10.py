from math import sqrt
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"point({self.x}, {self.y})"

def closes_points(points_list:list[point]):
    n = len(points_list)
    if (n <= 1):
        return 0
    
    min_dist = (points_list[1].x - points_list[0].x)**2 + (points_list[1].y-points_list[0].y)**2
    point1 = points_list[0]
    point2 = points_list[1]

    for i in range(n):
        for j in range(i+1,n):
            dx = (points_list[j].x - points_list[i].x)**2
            dy = (points_list[j].y-points_list[i].y)**2
            sq_dist = dx + dy
                         
            if (sq_dist < min_dist):
                point1 = points_list[i]
                point2 = points_list[j]

                min_dist = sq_dist

    return (point1,point2,sqrt(min_dist))

def bubble_sort(nums:list[int]):
    n = len(nums)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

def test_functions()->str:
    
    points:list[point] = [point(10,20),point(1009,100),point(5,6),point(99,9)]
    print(closes_points(points))
    
    numbers = [1,2,3,4,5,6,7,8,9]
    numbers.reverse()
    print(f"before sorting: {numbers}")
    bubble_sort(numbers)
    print(f"after sorting: {numbers}")

    return ""

if (__name__ == "__main__"):
    test_functions()