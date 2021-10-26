import matplotlib.pyplot as plt
import numpy as np
x_data = np.array([9,4,7,3,10,7,4,3,1,9])
y_data = np.array([45,24,59,28,91,28,42,18,14,82]) 
arr = np.linspace(1,10,100)
plt.plot(x_data,y_data,'rx')
plt.show()


# 決定 a 與 b 的起始點
b = 0
a = 0

# 決定 learning rate
lr = 0.00005

# 決定 iteration 的次數
iteration = 500

# 儲存每一次 iterate 後的結果
b_history = [b]
a_history = [a]

# 執行梯度下降
for i in range(iteration):
    b_grad = 0.0
    a_grad = 0.0
    
    # 計算損失函數分別對 a 和 b 的偏微分
    for n in range(len(x_data)):
        b_grad = b_grad  - 2.0*(y_data[n] - b - a*x_data[n])*1.0
        a_grad = a_grad  - 2.0*(y_data[n] - b - a*x_data[n])*x_data[n]
        
    # 更新 a, b 位置 
    b = b - lr * b_grad
    a = a - lr * a_grad
    
    # 紀錄 a, b 的位置 
    b_history.append(b)
    a_history.append(a)
print(a_history[-1],b_history[-1])
# 建立等高線圖


# 繪製 x 軸與 y 軸的標籤
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x_data,y_data,'rx')
plt.plot(arr,a_history[-1]*arr+b_history[-1])
plt.show()
