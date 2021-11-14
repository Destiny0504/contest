#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    int times = 0;
    cin >> times;

    for (int i = 0;i < times; i++)
    {
        int tmp = 0;
        cin >> tmp;
        int count_0 = 0;
        int count_1 = 0;
        
        for( int j = 0;j < tmp; j++)
        {
            int data = 0;
            cin >> data;
            if(data == 0)
                count_0++;
            else if(data == 1)
                count_1++;
        }
        //cout<<count_0<<"    "<<count_1<<endl;
  
        cout << (unsigned long long)(pow(2,count_0) * count_1)<< endl;

    }
}