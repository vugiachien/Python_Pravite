def transpose_matrix(matrix):
  """Trả về ma trận chuyển vị của matrix"""

  n = len(matrix)
  m = len(matrix[0])

  # Khởi tạo ma trận chuyển vị
  transposed_matrix = []
  for i in range(m):
    transposed_matrix.append([])
    for j in range(n):
      transposed_matrix[i].append(matrix[j][i])

  return transposed_matrix


# Nhập ma trận
n, m = map(int, input().split())
matrix = []
for i in range(n):
  matrix.append(list(map(int, input().split())))

# In ma trận chuyển vị
transposed_matrix = transpose_matrix(matrix)
for i in range(m):
  for j in range(n):
    print(transposed_matrix[i][j], end=" ")
  print()