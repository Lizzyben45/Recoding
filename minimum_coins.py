def minimum_coins(coins, amount):
    dp = [amount + 1] * (amount + 1)
    
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != amount + 1 else -1
print(minimum_coins([1, 2, 5], 11)) 
print(minimum_coins([30, 20, 17], 10))   
