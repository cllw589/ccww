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
