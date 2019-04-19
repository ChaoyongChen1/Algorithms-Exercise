#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
  01背包问题
  给定ItemCount个物品, 物品i的重量是Weights[i], 价值Values[i], 背包的容量为TotalWeight
  问应该如何选择装入背包的物品，使得背包内物品的总价值最大？

  Created by chaoyongchen on 2019/4/17.
  Copyright © 2019年 chaoyongchen. All rights reserved.
'''
def GetMax(RestWeight,Index):
	if Index==0:
		if RestWeight>=Weights[Index]:
			max_value=Values[Index]
		else: max_value=0
	elif RestWeight>=Weights[Index]:
		doPut=GetMax(RestWeight-Weights[Index],Index-1)+Values[Index]
		doNot=GetMax(RestWeight,Index-1)
		max_value=max(doPut,doNot)
	else:
		max_value=GetMax(RestWeight,Index-1)
	return max_value

if __name__ == '__main__':
	Num=4
	TotalWeight=10
	Values=[111,222,332,444]
	Weights=[1,3,5,6]
	print "总价值为： %d " %GetMax(TotalWeight,Num-1)