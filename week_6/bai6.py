
def gradient_descent(x, y, w_init, b_init, alpha, max_iter):
  """Tối ưu hóa w và b bằng thuật toán gradient descent"""

  w = w_init
  b = b_init

  for _ in range(max_iter):
    dw = 1/(2*len(x)) * sum([(c_i - y_i)**2 * x_i for c_i, y_i, x_i in zip(c, y, x)])
    db = 1/(2*len(x)) * sum(c_i - y_i for c_i, y_i in zip(c, y))
    w -= alpha * dw
    b -= alpha * db

  return w, b


def predict(x, w, b):
  """Dự đoán giá căn hộ"""

  c = [w * x_i + b for x_i in x]

  return c


def main():
  # Khởi tạo dữ liệu
  x = [20, 30, 40, 50, 60]
  y = [300, 400, 500, 600, 700]

  # Khởi tạo các giá trị ban đầu
  w_init = 0
  b_init = 0

  # Tốc độ học
  alpha = 0.01

  # Số lần lặp
  max_iter = 100

  # Tối ưu hóa w và b
  w, b = gradient_descent(x, y, w_init, b_init, alpha, max_iter)

  # In kết quả
  print(f"w = {w}, b = {b}")

  # Dự đoán giá căn hộ có diện tích 40 m2
  c = predict([40], w, b)
  print(f"Giá căn hộ có diện tích 40 m2 là: {c[0]}")


if __name__ == "__main__":
  main()