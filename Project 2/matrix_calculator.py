matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]
result_matrix = [[0, 0], [0, 0]]

for row_index in range(2):
    for col_index in range(2):
        result_matrix[row_index][col_index] = matrix_A[row_index][col_index] + matrix_B[row_index][col_index]

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

print("Matrix A:")
print_matrix(matrix_A)

print("\nMatrix B:")
print_matrix(matrix_B)

print("\nSum of Matrices (A+B):")
print_matrix(result_matrix)