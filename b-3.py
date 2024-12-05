gyou = int(input("行数を入力してください: "))
retsu = int(input("列数を入力してください: "))

for i in range(1, gyou + 1):
    for j in range(1, retsu + 1):
        result = f"{i} x {j} = {i * j:2}"
        print(f"{result:<7}", end=" | ")
    print()
