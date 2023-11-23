from datetime import datetime

while True:
    s = input()
    d, m , y = list(map(int, s.split('/')))
    if 1 <= d <= 31:
        break
    if 1 <= m <= 12:
        break
    if y >= 1000:
        break

    print("Invalid input")

time = datetime.strptime(s,r"%d/%m/%Y")
day_of_year = datetime(y, 12, 31)

days_remain = day_of_year - time

print(days_remain.days)