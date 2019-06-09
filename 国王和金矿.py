import copy

def good(n, w, g=[], p=[]):
    # n为金矿数，w为人数，g为金矿数组，p为人数数组
    arr = [0] * w
    for i in range(w):
        if (i + 1) >= p[0]:  # i为坐标， i+1为人数
            arr[i] = g[0]
    res = copy.deepcopy(arr)  # 深copy
    print(res)
    # 上面为只有一个金矿的情况

    for i in range(1, n):  # 金矿数
        for j in range(w):  # 人工数
            if (j + 1) < p[i]:  # j为坐标， j+1为人数
                arr[j] = res[j]  # 和上一次情况相同
            else:
                t = 0 if (j - p[i]) < 0 else j - p[i]  # 防止负数取到后面的值
                arr[j] = max(res[j], res[t] + g[i])  # 挖和不挖第i座金矿比较取大
                # res[t]+g[i] 为 挖第i座金矿的情况，res[已有人数 - 第i座所需人数]+第i座金子g[i]
        res = copy.deepcopy(arr)
        print(res)
    return res.pop()


if __name__ == '__main__':
    res = good(5, 10, [400, 500, 200, 300, 350], [5, 5, 3, 4, 3])
    print(res)
