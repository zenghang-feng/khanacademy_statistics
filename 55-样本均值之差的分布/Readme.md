1. 假设有随机变量X、Y，随机变量X的均值为mean_x，方差为var_x；随机变量Y的均值为mean_y，方差为var_y；  

2. 对随机变量X进行采样，样本容量为n，得到新的随机变量X_s；对随机变量Y进行采样，样本容量为m，得到新的随机变量Y_s;  
   X_s的均值为mean_x，方差为var_x/n；Y_s的均值为mean_y，方差为var_y/m;  

3. 定义新的随机变量 Z = X_s - Y_s,  
   随机变量Z的均值 mean_z = mean_x - mean_y，随机变量Z的方差为 var_z = var_x/n + var_y/m;
```
```
