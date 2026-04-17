

# def insertionSort(arr:list[int]):
#     length = len(arr)

#     for i in range(1,length):
#         val = arr[i]
#         j = i-1
        
#         while j >= 0 and arr[j] > val:
#             arr[j+1] = arr[j]
#             j-=1

#         arr[j+1] = val
            



# def test_functions()->str:
#     array:list[int] = [5,7,9,1,8,2,6,4,3]
#     print(f"before sorting: {array}")
#     insertionSort(array)
#     print(f"after sorting: {array}")


#     return ""

# if (__name__ == "__main__"):
#     test_functions()


from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Abdulhadi!")
        self.play(Write(text))
        self.wait(1)

