'''
2018.09.11
递归创建决策树

'''

def creatdataset(): #dataset 要求最后一列为类别标签列； lables与类别标签无关， 存储的是特征名称
	dataset = [[1, 1, 'yes'],
				[1, 1, 'yes'],
				[0, 1, 'no'],
				[0, 1, 'no']]
	labels = ['no surfacing', 'flippers']
	return dataset, labels

	
from math import log

def calcshannonEnt(dataset): # 计算的是H（Y）（以二分类为例） = -prob(1)*log(prob(1),2)-prob(0)*log(prob(1), 2)
	numEntries = len(dataset)
	lablecounts = {}
	for featvet in dataset:
		currentlabel = featvet[-1] #每个样本的类别标签
		if currentlabel not in lablecounts.keys():
			lablecounts[currentlabel] = 0
		lablecounts[currentlabel] += 1
	
	shannonEnt = 0.0
	for key in lablecounts:
		prob = float(lablecounts[key])/numEntries
		shannonEnt -= prob*log(prob, 2)
	return shannonEnt

def splitdataset(dataset, axis, value): #返回原dataset中样本属性 axis 等于 value 的样本集
	retdataset = []
	for featvec in dataset:
		if featvec[axis] == value:
			reducedfeatvec = featvec[ : axis]
			reducedfeatvec.extend(featvec[axis+1 : ])
			retdataset.append(reducedfeatvec) #下一个节点不可能再出现这个特征，且由于是递归，子孙节点不会再出现父母节点用过的特征
			                                  #但同级兄弟节点间有可能出现同一特征
	return retdataset

def choosebestfeaturetosplit(dataset): #即找出当前样本集的axis
	numfeatures = len(dataset[0]) - 1
	baseEntropy = calcshannonEnt(dataset)
	bestinfogain = 0.0; bestfeature = -1
	for i in range(numfeatures):
		featlist = [example[i] for example in dataset]
		uniquevalues = set(featlist)
		newEntropy = 0.0
		for value in uniquevalues:
			subdataset = splitdataset(dataset, i, value)  #找出当前特征下当前值的dataset
			prob = float(len(subdataset))/float(len(dataset))
			newEntropy += prob*calcshannonEnt(subdataset)
		infogain = baseEntropy - newEntropy
		if infogain > bestinfogain:
			bestinfogain = infogain
			bestfeature = i
	return bestfeature


import operator
def majoritycnt(classlist):
	classcount = {}
	for vote in classlist:
		if vote not in classcount.keys():
			classcount[vote] = 0
		classcount[vote] += 1
	sortedclasscount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedclasscount[0][0]

def createtree(dataset, lables):
	classlist = [example[-1] for example in dataset] # 所有数据集样本的标签组成的列表
	if classlist.count(classlist[0]) == len(classlist): #判断列表中所有的标签是否相同（判断方式略奇怪）
		return classlist[0] #返回叶节点， 即代表此叶节点的类别标签
	if len(dataset[0]) == 1: #数据集第一个样本的长度为1 即只含一个类别标签信息 特征已消耗完(上一个递归过程传递过来的刚好有一个特征可以划分)
		return majoritycnt(classlist) #返回叶节点， 返回的是其中最多类别的标签
	
	bestfeat = choosebestfeaturetosplit(dataset) #返回这个特征在样本集中的位置编号 x = [x1, x2, x3 ...]
	bestfeatlable = lables[bestfeat] #此标签存储的是特征的名字， 与类别标签无关
	
	mytree = {bestfeatlable: {}} #创建root或父母节点
	
	del(lables[bestfeat])  # 决定了特征被不断消耗，不会重复判断特征
	
	featvalues = [example[bestfeat] for example in dataset]
	uniquevals = set(featvalues)
	
	for value in uniquevals:
		sublables = lables[:]
		mytree[bestfeatlable][value] = createtree(splitdataset(dataset, bestfeat, value), sublables)
	
	return mytree # 当所有的递归过程进行完才会return整条tree
