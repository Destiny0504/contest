#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main(){
    int test;
    cin >>  test;
    unordered_map<string, vector<string>> m;
    for(int t=0;t<test;++t){
        string e;
        cin >> e;
        if(e=="IN"){
            string n;
            cin >> e;
            cin >> n;
            m[e].push_back(n);
        }else{
            cin >> e;
            if(m.find(e) == m.end())
                cout<<"CALL THE POLICE\n";
            else{
                const auto s = m[e].size();
                if(s==0)
                    cout<<"CALL THE POLICE\n";
                else{
                    sort(m[e].begin(), m[e].end());
                    cout<< e << ' ' <<m[e][0];
                    for(int i=1;i<s;++i)
                        cout<<' '<<m[e][i];
                    cout<<'\n';
                }
                
                m[e].clear();
            }
        }
    }
}