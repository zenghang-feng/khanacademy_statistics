```
import matplotlib.pyplot as plt

############################################################
# 需要可视化的数据
############################################################
stem = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
leaf = [0, 0, 2, 4, 7, 7, 9, 1, 1, 3, 8, 0]

############################################################
# 引用matplotlib绘图
############################################################
# 绘制茎图
# plt.stem(stem, leaf)
# 显示图像
# plt.show()

############################################################
# 通过打印字符串绘图
############################################################
dit = {}
length = len(stem)
for i in range(length):
    if stem[i] in dit:
        dit[stem[i]] = dit[stem[i]] + ', ' + str(leaf[i])
    else:
        dit[stem[i]] = str(leaf[i])

print("Stem | Leaf")
for k in dit:
    print("  ", k, "|", dit[k])
```

图像显示如下：  
![image](https://github.com/zenghang-feng/khanacademy_statistics/blob/main/08-茎叶图/pic1.png)
