def input_array(n):
  """Nhập mảng có n số"""

  array = []
  for i in range(n):
    array.append(int(input()))

  return array


def sum_from_start_to_x(array, x):
  """Tính tổng từ vị trí đầu đến vị trí x"""

  sum = 0
  for i in range(x):
    sum += array[i]

  return sum


# Nhập mảng có n số
n = int(input())
array = input_array(n)

# Nhập vị trí x
x = int(input())

# Tính tổng từ vị trí đầu đến vị trí x
sum = sum_from_start_to_x(array, x)