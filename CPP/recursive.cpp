#include <iostream>
using namespace std;
long fac(int);
int main()
{
    int n=5;
    long y;
    //cout <<"请输入";
    //cin >>n;
    y = fac(n);
    cout<<n<<"!="<<y<<endl;
    getchar();
    getchar();
    return 0 ;
}

long fac(int n)
{
    long f;
    if (n <0)
    {
        cout<<"错误！！！"<<endl;
    }
    else if(n== 0||n == 1) 
    f =1;
    else 
    f=fac(n-1)*n;
    return f;
}
