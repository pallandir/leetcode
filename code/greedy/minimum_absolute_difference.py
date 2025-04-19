def minimum_difference(numbers):
    if len(numbers) < 2:
        return 0

    numbers.sort()
    minimum_difference = float("inf")
    for index in range(1, len(numbers)):
        minimum_difference = min(
            minimum_difference, abs(numbers[index] - numbers[index - 1])
        )

    return minimum_difference


if __name__ == "__main__":
    print(minimum_difference([-2, 2, 4]))
