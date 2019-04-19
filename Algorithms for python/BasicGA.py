# -*- coding: UTF-8 -*-
"""
Visualize Genetic Algorithm to find a maximum point in a function.
可视化遗传算法去找到一个函数的最高点
"""
import numpy as np
import matplotlib.pyplot as plt
 
DNA_SIZE = 10            # DNA length
POP_SIZE = 100           # population size，种群中个体数目
CROSS_RATE = 0.8         # mating probability (DNA crossover)，0.8的概率进行交叉配对
MUTATION_RATE = 0.003    # mutation probability，变异强度
N_GENERATIONS = 300      #迭代次数
X_BOUND = [0, 5]         # x upper and lower bounds，指定x的取值范围
 
 
def F(x):
    return np.sin(10*x)*x + np.cos(2*x)*x     # to find the maximum of this function
 
 
# find non-zero fitness for selection
#我们都需要一个评估好坏的方程, 这个方程通常被称为 fitness适应度.
#为了找到下面这个曲线当中的最高点. 那么这个 fitness 方程可以定义为高度, 越高的点, fitness 越高.
def get_fitness(pred):
    "返回适应度值"
    return pred + 1e-3 - np.min(pred)#因为如果直接返回pred可能是负值，而我们在计算概率的时候不能为负值。
    #要进行处理，np.min表示取最小，为最大的负数，可以使全部只变成正的；1e-3为了让float进行相除防止小数点后的数被省略
 
 
# convert binary DNA to decimal and normalize it to a range(0, 5)
#对基因的翻译，如这里函数，x轴是实数，这里解释了如何将遗传0、1序列翻译成实数。用十进制二进制转换
#pop (population)是一个储存二进制 DNA 的矩阵, 他的 shape 是这样 (pop_size, DNA_size)
#这里DNA_SIZE，X_BOUND是超参数
def translateDNA(pop):
    "输入种群DNA矩阵，返回每一个人的十进制数"
    return pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2**DNA_SIZE-1) * X_BOUND[1]
    #dot()函数是矩阵乘,而*则表示逐个元素相乘
    #np.arange()函数返回一个有终点和起点的固定步长的排列
    #pop.dot(2 ** np.arange(DNA_SIZE)[::-1])已经转换成十进制
    #但是需要归一化到0~5,如有1111这么长的DNA,要产生的十进制数范围是[0, 15], 而所需范围是 [-1, 1],就将[0,15]缩放到[-1,1]这个范围
    #a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。所以你看到一个倒序
    #np.arange(DNA_SIZE)[::-1]得到10,9,8,...,0
 
#这里进行优胜劣汰的选择步骤
#适者生存的 select() 很简单, 我们只要按照适应程度 fitness 来选 pop 中的 parent 就好. fitness 越大, 越有可能被选到.
def select(pop, fitness):    # nature selection wrt pop's fitness
    "输入种群DNA矩阵和对应的适应度值，轮盘赌法选择DNA矩阵，矩阵大小不变，返回新选择的种群DNA矩阵"
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,p=fitness/fitness.sum())
    #这里概率不能为负，所以pred要进行非负处理
    #replace表示抽样后是否放回，这里为True表示有放回，则可能会出现相同的索引值
    # p 就是选它的比例，按比例来选择适应度高的,也会保留一些适应度低的，因为也可能后面产生更好的变异
    #np.random.choice表示从序列中取值  np.arange()函数返回一个有终点和起点的固定步长的排列
    return pop[idx]
 
#繁衍，交叉父母的基因
def crossover(parent, pop):     # mating process (genes crossover)
    "以当前一个人口基因为父亲，然后随机选择pop的另外一个人作为母亲进行杂交，返回杂交后的一个人口DNA序列"
    if np.random.rand() < CROSS_RATE: #这里是0.8的概率父亲会选择一个母亲进行交叉配对
        i_ = np.random.randint(0, POP_SIZE, size=1)                           #select another individual from pop选择母亲索引一个
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool) #得到一行[01001100]也是0、1为了选择哪些点进行交叉;然后进行布尔化
        parent[cross_points] = pop[i_, cross_points]
        #布尔型数组可以用于数组索引，布尔型数组长度必须跟被索引的轴长度一致
        #生成布尔数组可以组合应用多个布尔条件,使用&(和),|(或)之类的布尔算数运算符，python的关键字and和or在布尔型数组中无效
        #parent[cross_points]即parent列表中取出cross_points为True地方的值&&&&&！！！！
        #【母亲是pop的i_索引行DNA，选出母亲对应在cross_points为TRUE的地方的值】赋给【父亲DNA对应在cross_points选出为TRUE的地方的值】。
    return parent
 
#繁衍，有变异的基因会出现
#将某些 DNA 中的 0 变成 1, 1 变成 0
def mutate(child):
    "输入当前的一个人口DNA，突变，返回变异后的DNA序列"
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child

if __name__ == '__main__':
      
#产生离散均匀分布的整数，若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。
    pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))   # initialize the pop DNA
#pop = np.=random.randint(0,2,(1,DNA_SIZE).repeat(POP_SIZE,axis=0))这里是生成了一样的DNA，后面也可以随着变异变成不一样的
 
#[[01001100],
# [10111100],
# ...]
    plt.ion()       # something about plotting开启图像交互模式
 
    x = np.linspace(X_BOUND[0],X_BOUND[1],200)
#linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#X_BOUND = [0, 5],要产生200个样本点
#返回固定间隔的数据。他将返回num个等间距的样本，在区间[start,stop]中。其中，区间的结束端点可以被排除在外(用endpoint标识)
    plt.plot(x, F(x))
 
    for _ in range(N_GENERATIONS):
        F_values = F(translateDNA(pop))    # compute function value by extracting DNA传入到F函数
 
    # something about plotting
        if 'sca' in globals(): sca.remove()
        sca = plt.scatter(translateDNA(pop), F_values, s=200, lw=0, c='red', alpha=0.5); plt.pause(0.05)#plt.pause表示显示秒数
 
    # GA part (evolution)
        fitness = get_fitness(F_values) #计算适应度
        print("Most fitted DNA: ", pop[np.argmax(fitness), :])
        pop = select(pop, fitness)#这里选出了另外一种population
        pop_copy = pop.copy()# 备个份
        for parent in pop: #这里parent为遍历pop，一次为其中一行，而这里的pop是从原pop中按适应度概率有放回的选出了POP_SIZE行
            child = crossover(parent, pop_copy)#繁衍
            child = mutate(child) #进行变异
            parent[:] = child       # parent is replaced by its child# 宝宝变大人
 
    plt.ioff(); plt.show()
 
#在使用matplotlib的过程中，不能像matlab一样同时开几个窗口进行比较，可以采用交互模式，但是放在脚本里运行一闪而过，图像并不停留
#python可视化库matplotlib有两种显示模式：阻塞（block）模式&交互（interactive）模式
#在交互模式下：plt.plot(x)或plt.imshow(x)是直接出图像，不需要plt.show()
#如果在脚本中使用ion()命令开启了交互模式，没有使用ioff()关闭的话，则图像不会常留。防止这种情况，需要在plt.show()之前加上ioff()命令。
#在阻塞模式下：打开一个窗口以后必须关掉才能打开下一个新的窗口。这种情况下，默认是不能像Matlab一样同时开很多窗口进行对比的
#plt.plot(x)或plt.imshow(x)是直接出图像，需要plt.show()后才能显示图像
