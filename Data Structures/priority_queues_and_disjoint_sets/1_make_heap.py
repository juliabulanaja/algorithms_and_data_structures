class Heap:
    def __init__(self, array):
        self.H = array
        self.size = len(array)
        self.m = 0
        self.history = []
        self.make_heap()
        

    def swap(self, i: int, j: int) -> None:
        self.H[i], self.H[j] = self.H[j], self.H[i]
        self.history.append((i, j))
        self.m = self.m + 1

    def print_history(self):
        print(self.m)
        for i, j in self.history:
            print(f"{i} {j}")

    def get_parent_index(self, i: int) -> int:
        return i // 2

    def get_left_child_index(self, i: int) -> int:
        return i * 2

    def get_right_child_index(self, i: int) -> int:
        return i * 2 + 1

    def sift_up(self, i: int) -> None:
        parent_index = self.get_parent_index(i)

        while i > 0 and self.H[parent_index] > self.H[i]:
            self.swap(parent_index, i)
            i = parent_index
            parent_index = self.get_parent_index(i)

    def sift_down(self, i: int) -> None:
        min_index = i

        l = self.get_left_child_index(i + 1) - 1
        if l < self.size and self.H[l] <= self.H[min_index]:
            min_index = l

        r = self.get_right_child_index(i + 1) - 1
        if r < self.size and self.H[r] <= self.H[min_index]:
            min_index = r
        
        if i != min_index:
            self.swap(i, min_index)
            self.sift_down(min_index)
            

    def make_heap(self):
        
        i = self.size // 2 - 1
        while i >= 0:
            self.sift_down(i)
            i -= 1




if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split(' ')))

    # array = [5, 4, 3, 2, 1]

    my_heap = Heap(array)
    my_heap.print_history()


