def coin_row(coins):
    n = len(coins)
    if n == 0:
        return 0, []
    elif n == 1:
        return coins[0], [coins[0]]

    dp = [0] * n
    dp[0] = coins[0]
    dp[1] = max(coins[0], coins[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], coins[i] + dp[i-2])

    selected_coins = []
    i = n - 1
    while i >= 0:
        if i == 0:
            selected_coins.append(coins[0])
            break
        elif i == 1:
            if dp[1] == coins[1]:
                selected_coins.append(coins[1])
            else:
                selected_coins.append(coins[0])
            break
        else:
            if dp[i-1] > coins[i] + dp[i-2]:
                i -= 1
            else:
                selected_coins.append(coins[i])
                i -= 2

    selected_coins.reverse()
    return dp[-1], selected_coins


coins = [5, 1, 3, 6,2,7,1,4,8]
max_amount, selected_coins = coin_row(coins)
print("Maksimum para miktarı:", max_amount)
print("Seçilen paralar:", selected_coins)