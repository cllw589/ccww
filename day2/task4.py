import numpy as np

# 创建3x4的二维数组
arr = np.arange(1, 13).reshape(3, 4)

# 任务1：打印数组的形状、维度和数据类型
print("数组形状:", arr.shape)
print("数组维度:", arr.ndim)
print("数组数据类型:", arr.dtype)

# 任务2：将数组元素乘以2
arr *= 2
print("乘以2后的数组:\n", arr)

# 任务3：将数组重塑为4x3
reshaped_arr = arr.reshape(4, 3)
print("重塑后的数组:\n", reshaped_arr)




array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# 任务1：提取第2行所有元素（索引为1）
row2 = array[1, :]
print("第2行元素:", row2)

# 任务2：提取第3列所有元素（索引为2）
col3 = array[:, 2]
print("第3列元素:", col3)

# 任务3：提取子数组（第1、2行和第2、3列）
sub_array = array[1:4, 1:3]
print("子数组:\n", sub_array)

# 任务4：将大于10的元素替换为0
array[array > 10] = 0
print("修改后的数组:\n", array)



# 创建数组A和B
A = np.arange(1, 7).reshape(3, 2)
B = np.array([10, 20])

# 任务1：逐元素相加
sum_result = A + B
print("相加结果:\n", sum_result)

# 任务2：逐元素相乘
multiply_result = A * B
print("相乘结果:\n", multiply_result)

# 任务3：计算每一行与B的点积
dot_result = np.dot(A, B)
print("点积结果:", dot_result)