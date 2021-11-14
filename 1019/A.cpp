#include <iostream>

using namespace std;

// 定義對應表字元陣列
const char word[] = {'`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
                    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
                    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'',
                    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'};

int main(void)
{
	int stop ;
	cin >> stop ;
    char c;
    cin.get(c) ;
    while (stop != 0 && cin.get(c))
    {

        if (c == ' ')       { cout << c; }
        else if (c == '\n') { cout << endl; stop-- ;}
        else if (c == EOF) { cout << endl; stop-- ;}
        else
        {
            if ((c >= 65) && (c <= 90))
            {
                c = c + 32;
            }
            for (int i = 0; i < 47; i++)
            {
                if (word[i] == c)
                {
                    cout << word[i - 2];
                    break;
                }
            }
        }
    }
}