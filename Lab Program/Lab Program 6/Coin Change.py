def count_combinations(coins, target):
    # Recursive function to count combinations
    def count(coins, target, index):
        if target == 0:
            return 1
        if target < 0 or index >= len(coins):
            return 0
        # Count combinations including coins[index] and excluding coins[index]
        include_current_coin = count(coins, target - coins[index], index)
        exclude_current_coin = count(coins, target, index + 1)
        return include_current_coin + exclude_current_coin
    return count(coins, target, 0)
# Example usage
input_coins = [1, 2, 4]
amount = 4
possibilities = count_combinations(input_coins, amount)
print("Total number of possibilities:",possibilities)
