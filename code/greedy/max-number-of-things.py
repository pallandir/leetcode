def max_number_of_things(items_time, max_time):
    number_of_things = 0
    current_time = 0

    for item in sorted(items_time):
        if current_time + item <= max_time:
            number_of_things += 1
            current_time += item

    return number_of_things


if __name__ == "__main__":
    print(max_number_of_things([5, 3, 4, 2, 1], 6))
