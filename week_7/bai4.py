class Hiter:
    def __init__(self, id, ten, tuoi, gen):
        self.id = id
        self.ten = ten
        self.tuoi = tuoi
        self.gen = gen

    def __str__(self):
        return f"Hiter(id={self.id}, ten='{self.ten}', tuoi={self.tuoi}, gen={self.gen})"

    @staticmethod
    def danhSach():
        danhSachHiter = []
        for i in range(int(input("Nhập số lượng Hiter: "))):
            id = int(input("Nhập id: "))
            ten = input("Nhập tên: ")
            tuoi = int(input("Nhập tuổi: "))
            gen = int(input("Nhập gen: "))
            hiter = Hiter(id, ten, tuoi, gen)
            danhSachHiter.append(hiter)
        return danhSachHiter


class Ban:
    def __init__(self, idBan, tenBan, truongBan, thanhVien):
        self.idBan = idBan
        self.tenBan = tenBan
        self.truongBan = truongBan
        self.thanhVien = thanhVien

    def __str__(self):
        return f"Ban(idBan={self.idBan}, tenBan='{self.tenBan}', truongBan={self.truongBan}, thanhVien={self.thanhVien})"

    def dsHiter(self):
        for hiter in self.thanhVien:
            print(hiter)

    def xoa(self, hiter):
        self.thanhVien.remove(hiter)

    def add(self, hiter):
        if hiter not in self.thanhVien:
            self.thanhVien.append(hiter)


# Nhập danh sách Hiter
danhSachHiter = Hiter.danhSach()

# Nhập danh sách Ban
danhSachBan = []
for i in range(int(input("Nhập số lượng Ban: "))):
    idBan = int(input("Nhập id: "))
    tenBan = input("Nhập tên: ")
    truongBan = input("Nhập tên trưởng ban: ")
    thanhVien = []
    for j in range(int(input("Nhập số lượng thành viên: "))):
        id = int(input("Nhập id: "))
        ten = input("Nhập tên: ")
        tuoi = int(input("Nhập tuổi: "))
        gen = int(input("Nhập gen: "))
        hiter = Hiter(id, ten, tuoi, gen)
        if hiter in danhSachHiter:
            thanhVien.append(hiter)
    ban = Ban(idBan, tenBan, truongBan, thanhVien)
    danhSachBan.append(ban)

# Xóa thành viên trong ban
tenBan = input("Nhập tên ban cần xóa thành viên: ")
for ban in danhSachBan:
    if ban.tenBan == tenBan:
        id = int(input("Nhập id thành viên cần xóa: "))
        for hiter in ban.thanhVien:
            if hiter.id == id:
                ban.xoa(hiter)
                print(f"Đã xóa thành viên {hiter} khỏi ban {ban.tenBan}")
                break

# Thêm thành viên vào ban
tenBan = input("Nhập tên ban cần thêm thành viên: ")
for ban in danhSachBan:
    if ban.tenBan == tenBan:
        id = int(input("Nhập id thành viên cần thêm: "))
        for hiter in danhSachHiter:
            if hiter.id == id:
                ban.add(hiter)
                print(f"Đã thêm thành viên {hiter} vào ban {ban.tenBan}")
                break