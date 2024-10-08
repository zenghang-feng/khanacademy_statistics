# 1. 问题描述
## 1.1 原始分布情况定义
对于一个总统候选人，想研究男性和女性给该候选人投票的情况是否存在差异。

男性投票的情况服从伯努利分布，定义随机变量X，假设投票对应随机变量X的取值为1，未投票对应的随机变量X取值为0，投票的概率为p1，  
则有 E(X) = p1，VAR(X) = p1 * (1-p1);

女性投票的情况服也从伯努利分布，定义随机变量Y，假设投票对应随机变量X的取值为1，未投票对应的随机变量X取值为0，投票的概率为p2，    
则有 E(Y) = p2，VAR(Y) = p1 * (1-p2);


## 1.2 采样结果
现在分别抽取了1000个男性样本和1000个女性样本，男性样本中有642人投票给了上述候选人，女性样本中有591人投票给了上述候选人；  

求 p1 - p2 对应的95%的置信区间：

# 2. 程序实现
```
############################################################
# 样本信息：
############################################################
sample_nums = 1000
pos_1 = 642
pos_2 = 591

############################################################
# 计算样本均值和方差：
############################################################
p1_sample_sample = pos_1 / sample_nums
p2_sample_sample = pos_2 / sample_nums
# 用抽样分布样本的方差作为抽样分布总体方差的无偏估计
var1_sample_sample = p1_sample_sample * (1-p1_sample_sample) / sample_nums
var2_sample_sample = p2_sample_sample * (1-p2_sample_sample) / sample_nums

############################################################
# 构建置信水平为95的置信区间
############################################################
# 计算均值之差的抽样分布的均值和方差
dif_p = p1_sample_sample - p2_sample_sample
dif_var = var1_sample_sample + var1_sample_sample
# 对于均值之差的抽样分布：用样本方差作为总体方差的无偏估计,可得标准差
dif_std = dif_var ** 0.5
# 查表可得95%的概率对应的Z值为1.96
z_score = 1.96
ci_low = dif_p - z_score * dif_std
ci_up = dif_p + z_score * dif_std
# 可得95%的置信区间为 （0.009， 0.093）
```
