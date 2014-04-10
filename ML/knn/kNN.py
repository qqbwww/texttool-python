# coding=utf-8
# coding=utf-8
__author__ = 'qianqinbo'
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


group,labels = createDataSet()
print group
print labels


def classify0(inX, dataSet, labels,k):
    #距离计算
    """
    @rtype : object
    @param inX: 用于分类的输入向量
    @param dataSet: 输入的训练样本集
    @param labels: 标签向量
    @param k: 选择最近另据的数目
    @return:
    """
    #距离计算
    #获得形状：如果4*2矩阵，返回4，2， 然后在这里取shape[0],所以返回4
    datasetsize = dataSet.shape[0]
    print dataSet.shape
    # (4,2)
    #构造一个4*2矩阵,矩阵中的值为inX
    diffMat = tile(inX, (datasetsize,1)) - dataSet
    print diffMat
    #矩阵中值都平方
    sqdiffMat = diffMat ** 2
    print sqdiffMat

    sqldistances = sqdiffMat.sum(axis=1)
    print sqldistances
    distances = sqldistances ** 0.5
    #到这里通过欧氏距离公司计算出了距离

    #距离从小到大排序，sortedDistIndicies中存索引，按从小到大拍，也就是和输入分量接近的排前面
    sortedDistIndicies = distances.argsort()
    print sortedDistIndicies

    #确定前k个最小元素所在的主要分类
    classCount = {}
    for i in range(k):
        #先从排序中获得原始索引，从labels中获得定性的标识
        voteIlabel = labels[sortedDistIndicies[i]]
        #classCount作为数量字典，起计数作用
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    #排序 先获得classCount的遍历元素，将数量作为键值，逆向排序，值大排前面
    sortedClassCount = sorted(classCount.iteritems(),
                              key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

print classify0([0,0], group,labels,3)


def file2matrix(filename):
    #打开文件
    fr = open(filename)
    arrayOLines = fr.readlines()
    #得到文件行数
    numberOfLines = len(arrayOLines)
    #创建以零填充的的NumPy矩阵
    returnMat = zeros((numberOfLines,3))
    #类型标签向量
    classLabelVector = []
    index = 0
    #解析文件数据到列表
    for line in arrayOLines:
        line = line.strip();
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index + 1
    return returnMat,classLabelVector