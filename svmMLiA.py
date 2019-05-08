'''
2018.09.09
简化版SMO算法

辅助函数loaddataset

辅助函数selectJrand
外循环顺序选择阿尔法I， 内循环在（I,M）之间随机选择阿尔法J

辅助函数clipAlpha
对Alphanew修剪，使其位于（L，H）之间

'''
import numpy as np
from numpy import array, matrix
import random

def loadDataSet(filename):
	datamat = []; lablemat = []
	f = open(filename)
	for line in f:
		lineArr = line.strip().split('\t')
		datamat.append([float(lineArr[0]), float(lineArr[1])])
		lablemat.append(float(lineArr[2]))
	return datamat, lablemat
	
def selectJrand(i,m):
	j = i
	while(j == i):
		j = int(random.uniform(i,m))
	return j

def clipAlpha(aj, L, H):
	if aj > H:
		aj = H
	if aj < L:
		aj = L
	return aj

