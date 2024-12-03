gyou = int(input("行数を入力してください: "))
retsu = int(input("列数を入力してください: "))

for i in range(1, gyou + 1):
    for j in range(1, retsu + 1):
        print(i * j, end=" ")
    print()
