#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pylab as plt
CROSS_RATE = 0.8         # mating probability (DNA crossover)，0.8的概率进行交叉配对
MUTATION_RATE = 0.003    # mutation probability，变异强度
POP_SIZE=10
DNA_SIZE=4
X_BOUND = [0, 5]

def F(x): 
	return np.sin(10*x)*x + np.cos(2*x)*x

def translateDNA(pop):
    return pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2**DNA_SIZE-1) * X_BOUND[1]

def select(pop, fitness):    # nature selection wrt pop's fitness
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,p=fitness/fitness.sum())
    #这里概率不能为负，所以pred要进行非负处理
    #replace表示抽样后是否放回，这里为True表示有放回，则可能会出现相同的索引值
    # p 就是选它的比例，按比例来选择适应度高的,也会保留一些适应度低的，因为也可能后面产生更好的变异
    #np.random.choice表示从序列中取值  np.arange()函数返回一个有终点和起点的固定步长的排列
    return pop[idx]

def crossover(parent, pop):     # mating process (genes crossover)
    if np.random.rand() < CROSS_RATE: #这里是0.8的概率父亲会选择一个母亲进行交叉配对
        i_ = np.random.randint(0, POP_SIZE, size=1)                           #select another individual from pop选择母亲索引一个
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool) #得到一行[01001100]也是0、1为了选择哪些点进行交叉;然后进行布尔化
        parent[cross_points] = pop[i_, cross_points]
        #布尔型数组可以用于数组索引，布尔型数组长度必须跟被索引的轴长度一致
        #生成布尔数组可以组合应用多个布尔条件,使用&(和),|(或)之类的布尔算数运算符，python的关键字and和or在布尔型数组中无效
        #parent[cross_points]即parent列表中取出cross_points为True地方的值&&&&&！！！！
        #【母亲是pop的i_索引行DNA，选出母亲对应在cross_points为TRUE的地方的值】赋给【父亲DNA对应在cross_points选出为TRUE的地方的值】
    print "parent:"
    print parent
    return parent

def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    print "child:",
    print child
    return child

if __name__ == '__main__':
	x = np.linspace(0, 5, 500)
	y=F(x)
	array=np.arange(5)
	#print array
	DNA_bound=6
	pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE)) 
	print "初始种群：",
	print pop
	y=pop.dot(2 ** np.arange(DNA_SIZE)[::-1])
	print "10进制转换后：",
	print y
	fitness=translateDNA(pop)
	print "适应度函数：",
	print fitness
	pop_new=select(pop,fitness)
	print "自然选择过后的种群：",
	print pop_new
	pop_copy = pop_new.copy()
	print "循环len(pop_new)次结果："
	for parent in pop_new:
		child = crossover(parent, pop_copy)#繁衍
		print 
		child = mutate(child) #进行变异
		parent[:] = child 
	print "交叉变异后pop_new:",
	print pop_new 






	