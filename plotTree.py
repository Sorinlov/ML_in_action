'''
matplotlib 绘制树形图
涉及树的搜索遍历
'''

def getleafnum(myTree):
	numleafs = 0
	firststr = list(myTree.keys())[0]
	secondDict = myTree[firststr]    #多余？？？ 并非多余 寻找深度时正好忽略一层属性标签的深度，得出决策树的深度 
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			numleafs += getleafnum(secondDict[key])
		else:
			numleafs += 1
	return numleafs

def mygetleafnum(myTree):
	numleafs = 0
	for key in myTree.keys():
		if type(myTree[key]).__name__ == 'dict':
			numleafs += mygetleafnum(myTree[key])
		else:
			numleafs += 1
	return numleafs


def getTreedepth(myTree):
	maxdepth = 0
	firststr = list(myTree.keys())[0]
	secondDict = myTree[firststr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			thisdepth = 1 + getTreedepth(secondDict[key])
		else:
			thisdepth = 1
		if thisdepth > maxdepth:
			maxdepth = thisdepth
	return maxdepth

def mygettreedepth(myTree): #仅仅得出了有多少个嵌套字典 并非树的深度
    maxdepth = 0

    for key in myTree.keys():
        if type(myTree[key]).__name__ == 'dict':
            thisdepth = 1 + gettreedepth(myTree[key])
        else:
            thisdepth = 1
        if thisdepth > maxdepth:
            maxdepth = thisdepth
    return maxdepth

