#include <iostream>
#include <string>
#include <climits>
// #include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
    int n, W;
    int weight[100];
    int value[100];
    int dp[110][10010];

    cin >> n;
    cin >> W;

    for (int i = 0; i < n; i++)
    {
        cin >> weight[i] >> value[i];
    }

    for (int w = 0; w <= W; ++w)
        dp[0][w] = 0;

    for (int i = 0; i <= n; i++)
    {
        for (int w = 0; w <= W; w++)
        {
            if (w >= weight[i])
                dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w]);
        }
    }

    cout << dp[n][W] << endl;

    return 0;
}
