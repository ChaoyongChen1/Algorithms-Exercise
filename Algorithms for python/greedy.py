#!/usr/bin/python
# -*- coding: UTF-8 -*-
#i=7
def solve(money):
	sum=0
	list=range(7)
	list.reverse()
	for j in list:
		num_now=min(Counts[j],money/Values[j])
		money=money-Values[j]*num_now
		sum+=num_now
		print "面额为 %d 的钞票需要 %d 张" %(Values[j],num_now)
	if money > 0: 
		sum=-1
	return sum
if __name__ == '__main__':
	Values=[1,2,5,10,20,50,100]
	Total=432
	Counts=[100,1,100,66,10,5,1]
	print "至少需要 %d 张纸币" %solve(Total)