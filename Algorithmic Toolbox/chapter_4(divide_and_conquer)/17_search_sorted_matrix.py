from time import perf_counter


def search_sorted_matrix(matrix: list[list], q: int) -> int:

    for l, line in enumerate(matrix):

        if q < line[0] or q > line[-1]:
            continue

        left = 0
        right = len(line) - 1

        while left <= right:
            middle = (left + right) // 2

            if q == line[middle]:
                return l, middle
            elif q < line[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return -1


def binary_search_sorted_matrix(matrix: list[list], 
                                q: int, 
                                start_line: int = 0, 
                                end_line: int = None,
                                start_column: int = 0,
                                end_column: int = None
                                ) -> int:

    if end_line == None :
        end_line = len(matrix)
    if end_column == None:
        end_column = len(matrix[0])

    if end_line == start_line or ((end_line - start_line) < 1 and (end_column - start_column) < 1):
        return -1

    middle_l = (start_line + end_line) // 2
    middle_c = (start_column + end_column) // 2
    middle = matrix[middle_l][middle_c]

    if middle == q:
        return middle_l, middle_c

    elif middle > q:
        start_line1 = start_line
        end_line1 = middle_l
        start_column1 = start_column
        end_column1 = end_column

        start_line2 = middle_l
        end_line2 = end_line
        start_column2 = start_column
        end_column2 = middle_c
    else: 
        start_line1 = start_line
        end_line1 = middle_l + 1
        start_column1 = middle_c + 1
        end_column1 = end_column

        start_line2 = middle_l + 1
        end_line2 = end_line
        start_column2 = start_column
        end_column2 = end_column

    result1 = binary_search_sorted_matrix(matrix, q, start_line1, end_line1, start_column1, end_column1)
    result2 = binary_search_sorted_matrix(matrix, q, start_line2, end_line2, start_column2, end_column2)

    if result1 != -1:
        return result1
    if result2 != -1:
        return result2
        
    return -1


def binary_search_sorted_matrix_linear(matrix: list[list], q: int):
    rows = len(matrix)
    columns = len(matrix[0])

    r = 0
    c = columns - 1

    while r < rows and c < columns:
        value = matrix[r][c]
        if value == q:
            return r, c
        elif value < q:
            r += 1
        else: 
            c -= 1
    
    return -1

if __name__ == "__main__":

    matrix = [
        [1,  3,  4,  7,  13, 20, 27],
        [6,  13, 14, 21, 27, 34, 40],
        [10, 19, 21, 26, 31, 36, 42],
        [17, 25, 29, 36, 38, 40, 45],
        [20, 30, 37, 40, 45, 51, 56],
        [23, 36, 43, 49, 50, 56, 57],
        [26, 39, 47, 56, 58, 63, 69]
    ]

    q = 36

    start = perf_counter()
    result = search_sorted_matrix(matrix, q)
    print(f"{perf_counter() - start}. Result: {result}")

    start = perf_counter()
    result2 = binary_search_sorted_matrix(matrix, q)
    print(f"{perf_counter() - start}. Result: {result2}")

    start = perf_counter()
    result3 = binary_search_sorted_matrix_linear(matrix, q)
    print(f"{perf_counter() - start}. Result: {result3}")  