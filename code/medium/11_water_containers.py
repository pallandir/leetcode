def max_water_area(height: list[int]):
    left, right = 0, len(height) - 1
    max_content = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_content = max(max_content, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_content


if __name__ == "__main__":
    print(max_water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
