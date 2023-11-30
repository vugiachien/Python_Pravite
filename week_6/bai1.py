def MyMultiple(*args):
  """Tính tích các tham số truyền vào"""

  # Kiểm tra đầu vào
  for arg in args:
    if not isinstance(arg, (int, float)):
      raise TypeError("Các tham số phải là dạng số")

  # Tính tích các tham số
  result = 1
  for arg in args:
    result *= arg

  return result



