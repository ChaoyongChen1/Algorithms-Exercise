#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
sort.py
几种常用的排序算法
冒泡排序、简单选择排序、直接插入排序、快速排序

Created by chaoyongchen on 2019/4/17.
Copyright © 2019年 chaoyongchen. All rights reserved.
'''
#def show(array,size,start=0):
#	print array

'''
	新建一个sort类
	def swap(x,y):
	return y,x
'''
class sort:
	#list=[10, 3, 2, 1, 6, 4, 7, 5, 8, 9]
	#size=len(list)
	tuple=(10, 3, 2, 1, 6, 4, 7, 5, 8, 9)
	def __init__(self):
		print "原始序列： ",
		print sort.tuple
	def bubbleSort(self,list,size):
		for i in range(size):
			for j in range(size-1):
				if list[j]>list[j+1]: list[j],list[j+1]=list[j+1],list[j]
		print "冒泡排序： ",
		print list

	def selectSort(self,list,size):
		list_index=range(size)
		for i in list_index[:size-1]:
			indexMin=i
			j=i+1
			for j in list_index[j:]:
				if list[indexMin]>list[j]:indexMin=j
			if indexMin != i : list[i],list[indexMin]=list[indexMin],list[i]
		print "简单排序： ",
		print list



'''
def bubbleSort():
	list=[10, 3, 2, 1, 6, 4, 7, 5, 8, 9]
	size=len(list)
	print "原始序列： " ,
	print list
	for i in range(size):
		for j in range(size-1):
			if list[j]>list[j+1]:list[j],list[j+1]=list[j+1],list[j]
	print "冒泡排序： ",
	print list

def selectSort():
	list=[10, 3, 2, 1, 6, 4, 7, 5, 8, 9]
	size=len(list)
	print "原始序列： " ,
	print list
	list_index=range(size)
	for i in list_index[:size-1]:
		indexMin=i
		j=i+1
		for j in list_index[j:]:
			if list[indexMin]>list[j]:indexMin=j
		if indexMin != i : list[i],list[indexMin]=list[indexMin],list[i]
	print "简单排序： ",
	print list
'''
if __name__ == '__main__':
	list_ori=[10, 3, 2, 1, 6, 4, 7, 5, 8, 9]
	num=len(list_ori)
	bubble=sort()
	bubble.bubbleSort(list_ori,num)
	bubble.selectSort(list_ori[1:],num-1)


