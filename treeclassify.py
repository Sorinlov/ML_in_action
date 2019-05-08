'''
决策树中每两个字典构成树的一层，第一个字典的key总是属性名称节点，第二个字典的key总是属性的value值
'''



def classify(inputTree, featLabel, testVec):
    firststr = list(inputTree.keys())[0]
    secondDic = inputTree[firststr]
    featindex = featLabel.index(firststr)
    for key in secondDic.keys(): #第二个字典中的key是firststr属性名称下的属性值
        if testVec[featindex] == key:  #遍历属性值找到相同属性值类别
            if type(secondDic[key]).__name__ == 'dict':
                classlable = classify(secondDic[key], featLabel, testVec)
            else:
                classlable = secondDic[key]
    return classlable
