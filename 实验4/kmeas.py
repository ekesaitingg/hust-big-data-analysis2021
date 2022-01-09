import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import csv

def long_s(center, data):
    s = 0
    for i in range(1, 14):
        s += pow(center[i]-float(data[i]), 2)
    return s


def ssenum(m, data_min):   # 计算距离平方和SSE
    sse_num = [0, 0, 0]
    for i in range(m):
        sse_num[int(data_min[i, 0])-1] += data_min[i, 1]
    print('三个聚类的SSE依次为：', sse_num)
    sse = sse_num[0] + sse_num[1] + sse_num[2]
    print('SSE总和为:', sse)
    return sse


def get_points(m, data, j, data_min):
    point = []
    for i in range(m):
        if data_min[i, 0] == j + 1:  # 根据保存的信息进行分类
            point.append(data[i])
    return point


def get_acc(m, data, k, data_min):
    cluster = []
    hit = 0
    for j in range(k):
        cluster_tmp = [0, 0, 0]
        point = get_points(m, data, j, data_min)
        for item in point:
            cluster_tmp[int(item[0])-1] += 1
        hit += max(cluster_tmp)
    acc = hit / len(data)
    print('准确度为：', acc)    # 准确度为正确分类数与总数之比


if __name__ == '__main__':
    with open('normalizedwinedata.csv') as f:
        reader = csv.reader(f)
        data = []
        for j in reader:
            j = list(map(float, j))
            data.append(j)        # 从文件中读取数据并转换成浮点数.
    m = len(data)
    k = 3
    change = True
    data_min = np.mat(np.zeros((m, 2)))
    centers = []
    for i in range(k):
        c = []
        c.append(0)
        for j in range(13):
            c.append(rd.random())
        centers.append(c)         # 随机生成3个初始中心点
    count = 0
    while change:
        count += 1
        change = False   # 两次运算未出现差异时跳出循环
        for i in range(m):
            min_s = 10000000.0
            min_center = -1
            for j in range(k):
                distance = long_s(centers[j], data[i])
                if distance < min_s:
                    min_center = j + 1
                    min_s = distance             # 计算每个点到三个中心点的距离并得到最小值
            if data_min[i, 0] != min_center or data_min[i, 1] != min_s:
                data_min[i, :] = min_center, min_s
                change = True       # 更新每个点的最近中心点和距离信息
        for j in range(k):
            point = get_points(m, data, j, data_min)  # 根据求得的每个点的信息分类
            centers = np.array(centers)
            centers[j, :] = np.mean(point, axis=0)    # 计算出新的中心点,即列的均值
    print('循环次数为：', count)
    ssenum(m, data_min)
    get_acc(m, data, k, data_min)
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    print('请输入x,y轴对应的属性，范围1~13')
    print('x: ')
    x = int(input())
    print('y: ')
    y = int(input())
    for j in range(k):
        point = get_points(m, data, j, data_min)
        point = np.array(point)
        plt.scatter(point[:, x], point[:, y], c=colors[j])
    plt.scatter(centers[:, x], centers[:, y], marker='*', s=200, c='black')
    plt.show()
    with open("result.csv", 'w') as f:
        for i in range(m):
            f.write("{}\t,{}\n".format(data_min[i, 0], data_min[i, 1]))
    print('ok')
