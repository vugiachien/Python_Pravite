import math
def input_fractions(n):
  """Nhập vào n phân số"""

  fractions = []
  for i in range(n):
    a, b = map(int, input().split())
    fractions.append((a, b))

  return fractions


def add_fractions(fractions):
  """Tính tổng của n phân số"""

  # Tìm ước chung lớn nhất của các mẫu số
  gcd = fractions[0][1]
  for fraction in fractions:
    gcd = math.gcd(gcd, fraction[1])

  # Tính tổng của các tử số
  sum_numerator = 0
  for fraction in fractions:
    sum_numerator += fraction[0] * (gcd // fraction[1])

  # Trả về phân số tối giản
  return (sum_numerator // gcd, gcd)


def main():
  # Nhập vào số lượng phân số
  n = int(input())

  # Nhập vào các phân số
  fractions = input_fractions(n)

  # Tính tổng của các phân số
  sum_fraction = add_fractions(fractions)

  # In kết quả
  print(f"Tổng của các phân số là: {sum_fraction[0]}/{sum_fraction[1]}")


if __name__ == "__main__":
  main()