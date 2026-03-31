#include <iostream>
#include <string>
#include <climits>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
    int mod = 1000000009;

    int n, A;
    cin >> n >> A;

    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    int dp[101][1001];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= A; j++)
        {
            dp[i + 1][j] = dp[i][j];
            if (j >= a[i])
            {
                dp[i + 1][j] += dp[i][j - a[i]];
            }
        }
    }

    cout << dp[n][A] << endl;
}
