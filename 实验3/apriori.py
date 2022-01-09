import pandas as pd
import numpy as np


def data_set():
    data = pd.read_csv("Groceries.csv")
    # 读取列数据
    col_2 = data['items']
    data = np.array(col_2)
    # 将列数据转化为多维数组
    list_t1 = []
    for line in data:
        line = line.strip('{').strip('}').split(',')
        s = []
        for i in line:
            s.append(i)
        list_t1.append(s)
    data = list_t1  # 逐行获取商品信息，保存至list_t1中
    print(data[:4])
    return data


def Create_C1(data):
    # 创建C1
    c1 = set()
    for items in data:
        for item in items:
            item_set = frozenset([item])
            c1.add(item_set)
    print(c1)
    return c1


def is_apriori(ck_item, Lk):
    # 任何非频繁的(k-1)项集都不是频繁k项集的子集，因此Ck+1中每一个集合的子集都应该在Lk中
    for item in ck_item:
        sub_item = ck_item - frozenset([item])
        if sub_item not in Lk:
            return False
    return True


def Create_Ck(Lk, k):  # 通过合并Lk-1中前k-2项相同的项来获得Ck中的项
    Ck = set()
    len_Lk = len(Lk)
    list_Lk = list(Lk)
    for i in range(len_Lk):
        for j in range(i + 1, len_Lk):
            l1 = list(list_Lk[i])[0:k - 2]
            l2 = list(list_Lk[j])[0:k - 2]
            l1.sort()
            l2.sort()   # 为方便比较和后续操作，将前k-2项进行排序
            if l1 == l2:
                Ck_item = list_Lk[i] | list_Lk[j]
                if is_apriori(Ck_item, Lk):  # 舍弃非频繁项集
                    Ck.add(Ck_item)
    return Ck


def get_Lk(data_set, Ck, min_support, support_data):
    # 计算出现次数
    # len:多维数组返回最外围的大小
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1      # 计算项集在所有购物篮中出现的次数
    data_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / data_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / data_num  # 不满足最小支持度丢弃
    return Lk

def get_Rule(L, support_data, minconfidence):
    # 参数：所有的频繁项目集，项目集-支持度dic，最小置信度
    rule_list = []
    sub_set_list = []
    for i in range(len(L)):
        for frequent_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(frequent_set):       # 寻找上一轮循环中出现的frequent_set的子集
                    conf = support_data[frequent_set] / support_data[sub_set]  # conf(rule)=S(J)/S(J-j)
                    rule = (sub_set, frequent_set - sub_set, conf)
                    if conf >= minconfidence and rule not in rule_list:
                        rule_list.append(rule)
            sub_set_list.append(frequent_set)
    return rule_list


if __name__ == "__main__":
    data = data_set()
    minsupport = 0.005
    minconfidence = 0.5
    support_data = {}
    C1 = Create_C1(data)
    L1 = get_Lk(data, C1, minsupport, support_data)
    print('L1共包含 %d 项' % (len(L1)))
    Lk = L1.copy()
    L = []
    L.append(Lk)  # 末尾添加指定元素
    for k in range(2, 4):
        Ck = Create_Ck(Lk, k)
        Lk = get_Lk(data, Ck, minsupport, support_data)
        print('L%d共包含 %d 项' % (k, len(Lk)))
        Lk = Lk.copy()
        L.append(Lk)
    rule_list = get_Rule(L, support_data, minconfidence)
    print('关联规则总数为 %d ' % (len(rule_list)))
    with open('L1.csv', 'w') as f:
        for key in L[0]:
            f.write('{},\t{}\n'.format(key, support_data[key]))
    with open('L2.csv', 'w') as f:
        for key in L[1]:
            f.write('{},\t{}\n'.format(key, support_data[key]))
    with open('L3.csv', 'w') as f:
        for key in L[2]:
            f.write('{},\t{}\n'.format(key, support_data[key]))
    with open('rule.csv', 'w') as f:
        for item in rule_list:
            f.write('{}\t{}\t{}\t: {}\n'.format(item[0], "of", item[1], item[2]))
    print('运行结束')
