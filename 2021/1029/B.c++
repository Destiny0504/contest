#include<iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int times = 0;
    cin >> times;
    unsigned long long n, k;
    for(int i = 0;i < times; i++)
    {
        unsigned long long cur = 1, ans = 0, tmp = 1;

        cin >> n >> k;
        if(k == 1)
        {
            cout << n - 1 << endl;
            continue;
        }
        while(cur < n)
        {
            tmp = min(cur, k);
            if (tmp < k)
            {
                cur += tmp;
                ans += 1;
            }
            else
            {
                if ((n - cur ) % k == 0)
                {
                    ans += ((n - cur ) / k );
                    //((n - cur ) / k 
                    break;
                }
                else 
                {
                    ans += ((n - cur ) / k ) + 1;
                    //print(((n - cur ) / k ) + 1)
                    break;
                }
            }
        }
        cout << ans << endl;
    }
}