# 任务1：判断变量类型
x = 10
y = "10"
z = True
print(f"x的类型是：{type(x)}，值：{x}")
print(f"y的类型是：{type(y)}，值：{y}")
print(f"z的类型是：{type(z)}，值：{z}")

# 任务2：计算圆面积
radius = float(input("请输入圆的半径："))
area = 3.14 * radius ** 2
print(f"圆的面积为：{area:.2f}")

# 任务3：类型转换演示
num_str = "3.14"
num_float = float(num_str)
num_int = int(num_float)
print(f"字符串转浮点数：{num_float} (类型：{type(num_float)})")
print(f"浮点数转整数：{num_int} (类型：{type(num_int)})")
