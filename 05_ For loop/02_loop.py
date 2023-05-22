'''#include<stdio.h>
int main()
{
    int i;
    for (i = 1 ; i<=10 ; i++)
    {
        printf("%d\n",i);
    }
    return 0;
}
'''


numbers = [20,30,40,50,60]
for i in numbers:
    print(*[i])
    
for j in range(0,1):
    print(j)
    
x = [1,2,3,4,5]    
y = [1,2,3,4,5]    
z = [1,2,3,4,5]    

print(*[x])
print(*[y])
print(*[z])


for i in range(10):
    print(i, end=" ")
