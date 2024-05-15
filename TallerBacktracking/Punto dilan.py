# Dada una matriz arr de 
# tamaño n que contiene números enteros no negativos,
# la tarea es dividirla en dos conjuntos S1 y S2 de 
# manera que la diferencia absoluta entre sus 
# sumas sea mínima y encontrar la diferencia mínima

class Solution:
    def minDifference(self, arr, n):
        total_sum = sum(arr)
        dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, total_sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        min_diff = float('inf')
        for j in range(total_sum // 2, -1, -1):
            if dp[n][j]:
                min_diff = min(min_diff, total_sum - 2 * j)
                break
        
        return min_diff

# Ejemplo de uso
sol = Solution()
arr1 = [1, 6, 11, 5]
n1 = len(arr1)
print("Diferencia mínima:", sol.minDifference(arr1, n1))

arr2 = [1, 4]
n2 = len(arr2)
print("Diferencia mínima:", sol.minDifference(arr2, n2))
