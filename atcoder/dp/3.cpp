#include <iostream>
#include <string>
#include <climits>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
    int n, A;
    cin >> n >> A;

    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    bool dp[100][10000];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = true;

    for (int i = 0; i <= A; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (a[j] <= i)
            {
                dp[i + 1][j] = dp[i][j] || dp[i - a[j]][j];
            }
        }
    }

    if (dp[n][A])
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    return 0;
}
