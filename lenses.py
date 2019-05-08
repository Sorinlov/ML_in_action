from decision_tree import *
from treeclassify import *

f = open('lenses.txt')
dataset = [example.strip().split('\t') for example in f.readlines()]
traindataset = dataset[:20]
featurelables = ['age', 'prescript', 'astigmatic', 'tearRate']
lensestree = createtree(traindataset, featurelables)
print(lensestree)
featlabels = ['age', 'prescript', 'astigmatic', 'tearRate']

for i in range(20,24):
    result = classify(lensestree, featlabels, dataset[i])
    print(result)
    print(dataset[i][-1])
    print(featurelables)