def best_time_to_sell_stock(prices: list[int]):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        if (profit := (price - min_price)) > max_profit:
            max_profit = profit

    return max_profit


if __name__ == "__main__":
    print(best_time_to_sell_stock([7, 1, 5, 3, 6, 4]))
    print(best_time_to_sell_stock([7, 6, 4, 3, 1]))
