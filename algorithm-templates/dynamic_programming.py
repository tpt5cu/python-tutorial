"""
Common Dynamic Programming Patterns
"""



#Min/Max Path to reach a target
"""
Choose minimum (maximum) path among all possible paths before the current state, then add value for the current state.

eg. routes[i] = min(routes[i-1], routes[i-2], ... , routes[i-k]) + cost[i]


Problems;
1. Min Cost Climbing Stairs 
2. Minimum Path Sum 
3. Coin Change
931. Minimum Falling Path Sum Medium
983. Minimum Cost For Tickets Medium
650. 2 Keys Keyboard Medium
279. Perfect Squares Medium
1049. Last Stone Weight II Medium
120. Triangle Medium
474. Ones and Zeroes Medium
221. Maximal Square Medium
322. Coin Change Medium
1240. Tiling a Rectangle with the Fewest Squares Hard
174. Dungeon Game Hard
871. Minimum Number of Refueling Stops Hard
"""
for (int i = 1; i <= target; ++i) {
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] = min(dp[i], dp[i - ways[j]] + cost / path / sum) ;
       }
   }
}
 
return dp[target]

#Example in problem
def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp =[0] + [float("inf")]*amount
        for coin in coins:
            for j in range(coin,len(dp)):
                dp[j] = min(dp[j], dp[j-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1





#Distinct Ways

"""
Sum all possible ways to reach the current state.

eg. routes[i] = routes[i-1] + routes[i-2], ... , + routes[i-k]

Problems: 

70. Climbing Stairs easy
62. Unique Paths Medium
1155. Number of Dice Rolls With Target Sum Medium
688. Knight Probability in Chessboard Medium
494. Target Sum Medium
377. Combination Sum IV Medium
935. Knight Dialer Medium
1223. Dice Roll Simulation Medium
416. Partition Equal Subset Sum Medium
808. Soup Servings Medium
790. Domino and Tromino Tiling Medium
801. Minimum Swaps To Make Sequences Increasing
673. Number of Longest Increasing Subsequence Medium
63. Unique Paths II Medium
576. Out of Boundary Paths Medium
1269. Number of Ways to Stay in the Same Place After Some Steps Hard
1220. Count Vowels Permutation Hard
"""
for (int rep = 1; rep <= d; ++rep) {
   vector<int> new_ways(target+1);
   for (int already = 0; already <= target; ++already) {
       for (int pipe = 1; pipe <= f; ++pipe) {
           if (already - pipe >= 0) {
               new_ways[already] += ways[already - pipe];
               new_ways[already] %= mod;
           }
       }
   }
   ways = new_ways;
}

def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:return 1
        dp = [0]*(n+1)
        dp[1]=1
        dp[2] =2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
            












