#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
def fac(n):
	if n<0 :
		print "错误！！！"
	elif n==0 or n==1 :
		f=1
	else:
		f=fac(n-1)*n
	return 
if __name__ == '__main__':
	n=5
	y=fac(5)
	print "%d!=%d" %(n,y)
'''
def factorial(n):
	if n<0:
		print "错误！！！"
		
	elif n == 0 or n == 1:
		return 1
	else:
		return (n*factorial(n-1))

if __name__ == '__main__':
	num=10
	a = factorial(num)
	print "%d!=%d " %(num,a)
	
