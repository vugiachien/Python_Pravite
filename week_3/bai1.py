def nhap_diem():
    x = float(input())
    y = float(input())
    return x, y

def check(A, B, C):
    # Tính độ dài các cạnh của tam giác
    AB = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5
    AC = ((A[0] - C[0])**2 + (A[1] - C[1])**2)**0.5
    BC = ((B[0] - C[0])**2 + (B[1] - C[1])**2)**0.5

    # Kiểm tra tính hợp lệ của tam giác
    if AB + AC > BC and AB + BC > AC and AC + BC > AB:
        return "TAM GIÁC"
    else:
        return "KHÔNG PHẢI TAM GIÁC"

A = nhap_diem()
B = nhap_diem()
C = nhap_diem()


check(A, B, C)