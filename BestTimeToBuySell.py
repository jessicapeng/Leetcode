def maxProfit(self,prices):
    min_price = float('inf')
    amt = 0
    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > amt:
            amt = price - min_price
    return amt
