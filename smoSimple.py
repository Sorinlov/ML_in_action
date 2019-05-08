'''
2018.09.09
简化版SMO算法

'''
import numpy as np
from numpy import mat

def smoSimple(datamatin, classlables, C, toler, maxIter):
	datamatrix = mat(datamatin); lablemat = mat(classlables)
	b = 0; m, n = shape(datamatrix)
	alphas = mat(zeros(m, 1))
	iter = 0
	#for 循环中没有任何alpha改变的情况下 iter += 1
	#即iter为没有任何alpha改变的情况下遍历数据的次数
	
	while (iter < maxIter):
		alphapairchanged = 0
		for i in range(m):
			fxi = float(multiply(alphas, lablemat).T * (datamatrix*datamatrix[i, :].T)) + b 
			#所有样本数据集与Xi的内积
			Ei = fxi - float(lablemat[i])
			
			if ((lablemat[i]*Ei < -toler) and (alphas[i] < C)) or ((lablemat[i]*Ei > toler) and (alphas > 0)):
				j = selectJrand(i, m)
				#同样预测j的结果与误差
				fxj = float(multiply(alphas, lablemat).T * (datamatrix*datamatrix[j, :].T)) + b
				Ej = fxj - float(lablemat[j])
				
				alphaoldi = alphas[i].copy()
				alphaoldj = alphas[j].copy()
				#什么情况下需要用到copy？？？
				
				#计算L和H， 画方块图的那部分
				#异侧就相减， 同侧就相加
				if (lablemat[i] != lablemat[j]):
					L = max(0, alphas[j] - alphas[i])
					H = min(C, C + alphas[j] - alphas[i])
				else:
					L = max(0, alphas[j] + alphas[i] - C)
					H = min(C, alphas[j] + alphas[i])
				if L == H:
					print('L==H')
					continue 
					#此处继续下一个for循环
					#有何意义？仅仅是因为巧合L==H，导致单纯的无法进行优化？
				
				#计算eta（最有修改量）-（K11+K22-2K12）
				eta = 2.0 * datamatrix[i, :]*datamatrix[j, :].T - datamatrix[i, :]*datamatrix[i, :].T - datamatrix[j, :]*datamatrix[j, :].T
				if eta >= 0:
					print('eta >= 0')
					continue
				
				#计算alphaJnew的值
				alphas[j] -= lablemat[j]*(Ei - Ej)/eta
				alphas[j] = clipAlpha(alphas[j], H, L)
				
				#计算alphasJ的该变量，若不足则不再以此修改alphaI
				if (abs(alphas[j] - alphaoldj) < 0.00001):
					#此参数是否会改变？？？
					print('j not moving enough')
					continue
				
				#计算alphaInew的值
				alphas[i] += lablemat[i]*lablemat[j]*(alphaJold - alphas[j])
				
				#计算常数b
				#???b的公式仍需推导
				b1 = b - Ei - lablemat[i]*(alphas[i] -alphaoldi)*datamatrix[i, :]*datamatrix[i, :].T - lablemat[j]*(alphas[j] - alphaoldj)*datamatrix[i, :]*datamatrix[j, :].T
				b2 = b - Ej - lablemat[i]*(alphas[i] -alphaoldi)*datamatrix[j, :]*datamatrix[i, :].T - lablemat[j]*(alphas[j] - alphaoldj)*datamatrix[j, :]*datamatrix[j, :].T
				if (0 < alphas[i]) and (C > alphas[i]):
					b = b1
				elif (0 < alphas[j]) and (C > alphas[j]):
					b = b2
				else:
					b = (b1 + b2)/2.0
				
				#至此成功改变一对alpha
				alphapairchanged += 1
				print('iter: %d i:%d, pairs changed %d' % (iter, i, alphaPairsChanged))
				
		if (alphaPairsChanged == 0):
			iter += 1
		else:
			iter = 0
		print('iteration number: %d' % iter)
	 return b, alphas

		