import random


def main():
    N = int(input("サイコロの面の数は？:"))
    M = int(input("何回振りますか？:"))

    results = [random.randint(0, N) for _ in range(M)]
    print(results)


if __name__ == "__main__":
    main()
