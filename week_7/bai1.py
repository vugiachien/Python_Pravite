class Pycon:
    # Biến class để lưu trữ tổng số Pycon
    count = 0

    def __init__(self, name, age):
        # Tăng id tự động
        Pycon.count += 1
        self.id = Pycon.count
        self.name = name
        self.age = age

    def __str__(self):
        return f"Id {self.id}|| {self.name} || {self.age} tuổi"

    @classmethod
    def average_age(cls, pycons):
        total_age = sum(pycon.age for pycon in pycons)
        return total_age / len(pycons)

# Hàm main
def main():
    n = int(input("Nhập số lượng Pycon: "))
    pycons = []
    for i in range(n):
        name = input(f"Nhập tên của Pycon thứ {i+1}: ")
        age = int(input(f"Nhập tuổi của Pycon thứ {i+1}: "))
        pycon = Pycon(name, age)
        pycons.append(pycon)

    # In thông tin Pycon
    for pycon in pycons:
        print(pycon)

    # Tính trung bình độ tuổi của Pycon
    average_age = Pycon.average_age(pycons)
    print(f"Trung bình độ tuổi của các Pycon: {average_age}")

# Chạy hàm main
if __name__ == "__main__":
    main()