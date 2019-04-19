//
//  sort.cpp
//  几种常用的排序算法
//  冒泡排序、简单选择排序、直接插入排序、快速排序
//
//  Created by chaoyongchen on 2019/4/17.
//  Copyright © 2019年 chaoyongchen. All rights reserved.
//
#include<iostream>
using namespace std;

// 输出排序后的结果show()
void show(int *array,int size,int start=0){
	for(int i=start;i<size;i++)
		cout<<array[i]<<" ";
	cout<<"\n";
}
// 交换两个元素swap()
void swap(int& x,int& y){
	int temp=x;
	x=y;
	y=temp;

}
//冒泡排序算法bubbleSort()
void bubbleSort(){
	const int size=10;
	int array[size]={10, 3, 2, 1, 6, 4, 7, 5, 8, 9}; 
	cout<<"冒泡排序： "<<endl;
	show(array,size);
	for (int i=0;i<size;i++){
		for(int j=0;j<size-1;j++){
			if (array[j]>array[j+1]) 
				swap(array[j],array[j+1]);
		}
	}
	show(array,size);
}

/************************************
 * 简单选择排序selectSort()
 * 稳定排序，O{n^2} ~ O{n^2}
 * 从首位开始，循环一次找出一个比首位小的值，交换
 ************************************/
void selectSort(){
	const int size=10;
	int array[size]={10,3,2,1,6,4,7,5,8,9}; 
	cout<<"简单选择排序:"<<endl;
	show(array,size);
	
	for(int i=0;i<size-1;++i){
		int indexMin=i;
		//找到最小值下标
		for(int j=i+1;j<size;++j){
			if(array[indexMin]>array[j])
				indexMin=j;
			
		}
		if(indexMin!=i)
		//交换最小值与当前值
		swap(array[i],array[indexMin]);
	}

	show(array,size);
	


}
int main(int argc, char const *argv[])
{
	
    bubbleSort();
	selectSort();
	return 0;
}