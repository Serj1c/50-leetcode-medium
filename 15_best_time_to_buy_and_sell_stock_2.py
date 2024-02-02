def max_profit(prices) -> int:
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]

    return max_profit


print(max_profit([7,1,5,3,6,4]))