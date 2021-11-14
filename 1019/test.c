#include <stdio.h>

int main()
{
    
    int i = 0, J = 0, R = 0, answer = 0, record = 0;
    scanf("%d %d",&J, &R);
    while((0 != J) && (0 != R))
    {
        //printf("%d %d\n",J, R);
        int player[500] = {0};
        
        for(i = 0; i < R * J; i++)
        {
            int tmp = i % J, data = 0;
            //printf("%d\n",player[tmp]);
            scanf("%d", &data);
            //printf("%d\n",data);
            player[tmp] = player[tmp] + data;
        }
        for(i = 0; i < J; i++)
        {
            if(player[i] >= record)
            {
                answer = i + 1;
                record = player[i];
            }
        }
        printf("%d\n",answer);
        record = 0;
        answer = 0;
        scanf("%d %d\n",&J, &R);
    }
}