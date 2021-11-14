#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int times = 0;
    cin >> times;
    for(int i = 0;i < times; i++)
    {
        unsigned long long total = 0, killed = 0, tmp_ans = 0;
        unsigned long long deepth = 0, step = 0, tmp = 1, height = 0;
        unsigned long long tmp_list[51] = {1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471, 274877906943, 549755813887, 1099511627775, 2199023255551, 4398046511103, 8796093022207, 17592186044415, 35184372088831, 70368744177663, 140737488355327, 281474976710655, 562949953421311, 1125899906842623, 2251799813685247};
        cin >> deepth >> step;

        total = (pow(2,deepth) - 1);
        if (int(log2(step)) >= deepth - 1)
        {
                tmp_ans = deepth;
                killed = tmp_list[deepth - 1];
        }
        else
        {
            tmp_ans = int(log2(step));
            killed = tmp_list[tmp_ans];
            tmp_ans = tmp_ans + 1;
        }
        if((total - killed) % step == 0)
            tmp_ans = tmp_ans + (unsigned long long)((total - killed) / step);
        else
            tmp_ans = tmp_ans + (unsigned long long)((total - killed) / step) + 1;
        
        cout << tmp_ans << endl;
    }
}