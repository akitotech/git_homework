def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value


def find_min(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value


def calculate_avg(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def main():
    input_string = input("データを入力してください(スペース区切り) > ")
    numbers = [int(x) for x in input_string.split()]

    total = calculate_sum(numbers)
    max_value = find_max(numbers)
    min_value = find_min(numbers)
    average = calculate_avg(numbers)

    print(f"合計値: {total}")
    print(f"最大値: {max_value}")
    print(f"最小値: {min_value}")
    print(f"平均値: {int(average)}")


if __name__ == "__main__":
    main()
