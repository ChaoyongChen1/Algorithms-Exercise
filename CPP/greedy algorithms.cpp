//
//  main.cpp
//  贪心算法(greedy algorithm)
//  钱币找零问题
//  假设有i种纸币，Values[i]元的纸币有Counts[i]张。现在要用这些钱来支付Total元，至少要用多少张纸币？
//
//  Created by chaoyongchen on 2019/4/17.
//  Copyright © 2017年 chaoyongchen. All rights reserved.
//

#include <iostream>
using namespace std;
//定义纸币种类和面额 1，2，5，10，20，50，100
const int i=7;
const int Values[i]={1,2,5,10,20,50,100};
//设置目标金额
int Total=432;
int Counts[i]={100,1,100,66,10,5,1};

//纸币i的张数 100, 1, 100, 66, 10, 5, 1


// 求解函数solve(),每次都用最大面额，输出每种纸币的张数和总额，用到了min（x,y）函数，return 纸币张数
int solve(int money)
{
   int sum=0;
   for(int j=6;j>=0;j--){
      int num_now=min(Counts[j],money/Values[j]);
      
      money=money-Values[j]*num_now;
      sum+=num_now;
      cout<<"面额为 "<<Values[j]<<" 的钞票需要 "<<num_now<<" 张"<<endl;
      
   }
   if(money > 0) sum = -1;
   return sum;
}

//main(),显示需要的纸币张数
int main(int argc, char const *argv[])
{
   cout<<"至少需要"<<solve(Total)<<"张纸币"<<endl;
   return 0;
}