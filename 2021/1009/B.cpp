#include<iostream>
using namespace std;

int main()
{
    int times = 0, pass = 0, answer = 0;
    cin >> times >> pass;

    for(int i = 0; i < times; i++)
    {
        int tmp = 0;
        cin >> tmp;
        if (tmp < pass)
            answer++;
    }
    cout << answer << endl;
}