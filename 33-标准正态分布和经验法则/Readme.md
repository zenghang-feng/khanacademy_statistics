```
# 标准正态分布：均值为0，标准差为1的正态分布
mean = 0
std = 1

# 经验法则：对于正态分布，正负1个标准差内的概率约为0.68；正负2个标准差内的概率为0.95；正负3个标准差内的概率约为0.997。

# 1. P(X<1)
z1 = 1
# z1 = 1，根据经验法则和正态分布概率密度函数的对称性
p1 = 1 / 2 + 0.68 / 2
print("P(X<1) =", p1)

# 2. P(X<-1)
z2 = -1
# z2= -1
p2 = (1 - 0.68) / 2
print("P(X<-1) =", p2)

# 3. mean
print("mean:", mean)

# 4. std
print("std:", std)

# 5. P(X>2)
z5 = 2
# 根据经验法则和正态分布概率密度函数的对称性
p5 = 1 - (1 + 0.95) / 2
print("P(X>2) =", p5)
```
