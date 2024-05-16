def max_profit(prices, fee: int) -> int:
    balance_after_buy = float('-inf')
    balance_after_sell = 0
    for price in prices:
        next_buy = max(balance_after_buy, balance_after_sell - (price+fee))
        next_sell = max(balance_after_sell, balance_after_buy + price)

        balance_after_buy = next_buy
        balance_after_sell = next_sell
    return balance_after_sell


print(max_profit([1,3,2,8,4,9], 2))
print(max_profit([1,3,7,5,10,3], 3))