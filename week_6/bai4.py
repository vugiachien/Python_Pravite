import math
def read_coordinates(file_name):
  """Đọc tọa độ của 2 điểm từ tệp input.txt"""

  with open(file_name, "r") as file:
    data = file.readlines()

  # Xác định số dòng
  n_lines = len(data)

  # Khởi tạo mảng tọa độ
  coordinates = []
  for i in range(n_lines):
    coordinates.append(data[i].split())

  # Loại bỏ ký tự xuống dòng
  for i in range(n_lines):
    coordinates[i] = coordinates[i][:-1]

  return coordinates


def calculate_distance(coordinates):
  """Tính khoảng cách giữa 2 điểm"""

  # Lấy tọa độ x và y của điểm A
  x_a = float(coordinates[0][1])
  y_a = float(coordinates[0][2])

  # Lấy tọa độ x và y của điểm B
  x_b = float(coordinates[1][1])
  y_b = float(coordinates[1][2])

  # Tính khoảng cách
  distance = math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2)

  # Làm tròn đến số thập phân thứ 2
  distance = round(distance, 2)

  return distance


def write_to_file(file_name, coordinates, distance):
  """Ghi kết quả ra tệp output.txt"""

  with open(file_name, "w") as file:
    file.write("A(2.5, 4) B(3, 5) AB = {0:.2f}\n".format(distance))