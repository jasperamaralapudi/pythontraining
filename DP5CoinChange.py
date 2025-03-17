def rec_coin_change(coins,amount):
    if amount==0:
        return 0
    min_coins=float('inf')
    for coin in coins:
        if amount>=coin:
            min_coins=min(min_coins,1+rec_coin_change(coins, amount-coin))
    return min_coins if min_coins!=float('inf') else -1
def dp_coin_change(coins, amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i]=min(dp[i],1+dp[i-coin])
    return dp[amount] if dp[amount]!=float('inf') else -1
def optimized_coin_change(coins, amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for i in range(1, amount+1):
        for coin in coins:
            if i>=coin:
                dp[i]=min(dp[i],1+dp[i-coin])
    return dp[amount] if dp[amount]!=float('inf') else -1
coins=[1,2,5]
amount=11
print('Minimum Coins(Recursive Approach):',rec_coin_change(coins,amount))
print('Minimum Coins(Tabulation Approach):',dp_coin_change(coins, amount))
print('Minimum Coins(Optimized Approach):',optimized_coin_change(coins, amount))