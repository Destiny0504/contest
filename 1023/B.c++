#include<iostream>
using namespace std;

int main()
{   
    int column = 0, row = 0;
    long long data[50][50] = {0};
    bool ans = true;

    cin >> column >> row;
    //cout << column << row <<endl;
    for(int i = 0;i < column; i++)
    {
        for(int j = 0;j < row; j++)
        {
            cin >> data[i][j]; 
        }
    }
    
    for(int i1 = 0;i1 < column - 1; i1++)
    {
        for(int i2 = i1 + 1;i2 < column; i2++)
        {
            for(int j1 = 0;j1 < row - 1; j1++)
            {
                for(int j2 = j1 + 1;j2 < row; j2++)
                {
                    //cout<<i1<<i2<<j1<<j2<<endl;
                    if(data[i1][j1] + data[i2][j2] > data[i1][j2] + data[i2][j1])
                    {
                        ans = false;
                        //cout<<data[i1][j1]<<data[i2][j2]<<data[i1][j2]<<data[i2][j1]<<endl;
                    }
                       
                }
            }
        }
    }
    if(ans)
        cout<<"Yes"<<endl;
    else
        cout<<"No"<<endl;
    
}