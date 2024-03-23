# if len(A[0]) != len(B):
#     raise ValueError("Matrices must have the same number of columns.")

#   result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

#   for i in range(len(A)):
#     for j in range(len(B[0])):
#       for k in range(len(B)):
#         result[i][j] += A[i][k] * B[k][j]

#   return result


# # Example usage:

# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# print(dot_product(A, B))


