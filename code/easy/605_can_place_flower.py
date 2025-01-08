def can_place_flower(flowerbed: list[int], n: int):
    flowerbed = [0] + flowerbed + [0]
    for index in range(1, len(flowerbed) - 1):
        if n == 0:
            return True

        if (
            flowerbed[index - 1] == 0
            and flowerbed[index] == 0
            and flowerbed[index + 1] == 0
        ):
            flowerbed[index] = 1
            n -= 1

    return n <= 0


if __name__ == "__main__":
    print(can_place_flower([1, 0, 0, 0, 1], 1))
    print(can_place_flower([1, 0, 0, 0, 1], 2))
    print(can_place_flower([0, 1, 0], 1))
