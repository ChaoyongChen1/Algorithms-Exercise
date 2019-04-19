//  01背包问题
//  给定ItemCount个物品, 物品i的重量是Weights[i], 价值Values[i], 背包的容量为TotalWeight
//  问应该如何选择装入背包的物品，使得背包内物品的总价值最大？

//  Created by chaoyongchen on 2019/4/17.
//  Copyright © 2019年 chaoyongchen. All rights reserved.
//
#include<iostream>
using namespace std;

 // 物品数量
const int Num=4;
 // 背包容量
const int TotalWeight=10;
// 物品i的价值
int Values[Num] = {111, 222, 332, 444}; 
// 物品i的重量
int Weights[Num] = {1, 3, 5, 6};


// GetMax(),输入总重量和物品数，返回max[][]
int GetMax(int RestWeight,int Index){
	int max_value;
	if(Index==0){
		if(RestWeight>=Weights[Index]) max_value=Values[Index];
		else max_value=0;
	}
	else if(RestWeight>=Weights[Index]){
		int doPut=GetMax(RestWeight-Weights[Index],Index-1)+Values[Index];
		int doNot=GetMax(RestWeight,Index-1);
		max_value=max(doPut,doNot);
	}
	else
		max_value=GetMax(RestWeight,Index-1);



	return max_value;
}

//main()
int main(int argc, char const *argv[])
{
	
	cout<<"总价值为： "<<GetMax(TotalWeight,Num)<<endl;
	return 0;
}