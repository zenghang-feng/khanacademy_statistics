############################################################
# 样本信息：
############################################################
mean_sample_1 = 9.31
std_sample_1 = 4.67
mean_sample_2 = 7.4
std_sample_2 = 4.04

############################################################
# 假设检验
############################################################
# 原假设：mean_sample_1 - mean_sample_2 = 0
# 备择假设：mean_sample_1 - mean_sample_2 > 0
# 显著性水平 α = 0.05
# 计算统计量 =================================================
# 样本均值之差的采样
mean_sample_dif = mean_sample_1 - mean_sample_2
# 样本均值之差的标准差采样（作为样本均值之差抽样分布的无偏估计）
mean_sample_dif_std = ((std_sample_1**2)/100 + (std_sample_2**2)/100) ** 0.5
# 根据置信水平计算查询Z表时所需的边界；查表可得Z值为1.65
a_2 = 1 - 0.05
z_score = 1.65
# 均值之差的临界值为
mean_sample_dif_b = z_score * mean_sample_dif_std
# mean_sample_dif = 1.91；mean_sample_dif_b = 1.01
# 样本均值之差的采样值 > 样本均值之差的临界值，所以在5%的显著性水平下，拒绝原假设
