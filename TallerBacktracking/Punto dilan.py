# Dada una matriz arr de 
# tamaño n que contiene números enteros no negativos,
# la tarea es dividirla en dos conjuntos S1 y S2 de 
# manera que la diferencia absoluta entre sus 
# sumas sea mínima y encontrar la diferencia mínima

class Solution {
public:
    int minDifference(int arr[], int n)  {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }
        
        bool dp[n + 1][sum + 1];
        for (int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum; j++) {
                if (arr[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        int minDiff = INT_MAX;
        for (int j = sum / 2; j >= 0; j--) {
            if (dp[n][j]) {
                minDiff = min(minDiff, sum - 2 * j);
                break;
            }
        }
        
        return minDiff;
    }
};
