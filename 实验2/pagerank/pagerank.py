import numpy as np

if __name__ == '__main__':
    f = open('sent_receive.csv')
    edges = [line.strip('\n').split(',') for line in f]
    nodes = []
    for edge in edges:
        if edge[1] not in nodes:
            nodes.append(edge[1])
        if edge[2] not in nodes:
            nodes.append(edge[2])

    print(nodes)  # 找到有向图中的所有结点，同时规定矩阵的顺序

    N = len(nodes)
    L = len(edges)
    print(N)
    print(L)
    M = np.zeros([N, N])
    for edge in edges:
        start = nodes.index(edge[1])
        end = nodes.index(edge[2])
        M[end, start] = 1  # 初始化M矩阵

    for j in range(N):
        sum_of_col = sum(M[:, j])
        for i in range(N):
            if M[i, j]:
                M[i, j] /= sum_of_col  # 构造M矩阵,M矩阵每一列的和为1

    r = np.ones(N) / N
    next_r = np.zeros(N)
    e = 300000  # 误差初始化
    k = 0  # 记录迭代次数
    b = 0.85

    while e > 0.00000001:  # 开始迭代
        next_r = np.dot(M, r) * b + (1-b) / N * np.ones(N)   # 迭代公式
        sum_of_col = sum(next_r)
        next_r = next_r / sum_of_col
        e = next_r - r
        e = max(map(abs, e))  # 计算误差
        r = next_r
        k += 1

    print('迭代次数: %s' % str(k))
    print(r)
    print("r元素之和为：%f" % sum(r))

