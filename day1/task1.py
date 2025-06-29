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

# 任务4：输出1-100的素数
print("\n1-100的素数：")
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

# 任务5：斐波那契数列前20项
print("\n\n斐波那契数列前20项：")
a, b = 0, 1
for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b

# 任务6：条件求和
print("\n\n1-10000满足条件的数字和：")
total = 0
n = 1
while n <= 10000:
    if (n % 3 == 0 or n % 5 == 0) and n % 15 != 0:
        total += n
    n += 1
print(total)