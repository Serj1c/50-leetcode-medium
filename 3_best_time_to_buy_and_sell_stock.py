def max_profit(prices) -> int:
    if len(prices) < 1:
        return 0
    min_price = prices[0]
    profit = 0

    for p in prices:
        if p < min_price:
            min_price = p
            continue
        if p - min_price > profit:
            profit = p - min_price
    return profit


print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))
        