import numpy as np
import matplotlib.pyplot as plt

# 1. 生成年份数据（2000 - 2020 年，转成字符串类型）
year = np.arange(2000, 2021).astype(np.str_)

# 2. 生成月份数据（随机 1 - 12 月，转成字符串类型，共 20 个）
month = np.random.randint(1, 13, size=20).astype(np.str_)

# 3. 生成日期数据（随机 1 - 31 日，转成字符串类型，共 20 个）
day = np.random.randint(1, 31, size=20).astype(np.str_)

# 4. 组合年月日，生成完整日期字符串数组
date = np.array([])
for i in range(20):
    # 拼接单个日期的年、月、日部分
    single_date_parts = np.array([year[i], month[i], day[i]])
    # 用 '/' 连接成完整日期格式，如 '2000/1/1'
    combined_date = '/'.join(single_date_parts)
    date = np.append(date, combined_date)

# 5. 生成随机销量数据（范围 500 - 2000，数量和日期数量一致）
sales = np.random.randint(500, 2000, size=len(date))

# 6. 绘制图形
# 设置 x 轴刻度，每隔 2 个显示，旋转 45 度，红色字体，让日期显示更美观
plt.xticks(range(0, len(date), 2), ['日期:%s' % date[i] for i in range(0, len(date), 2)], rotation=45, color='red')
# 绘制折线图，x 轴为日期，y 轴为销量
plt.plot(date, sales)
# 显示图形（执行这行才会弹出绘制的图，之前代码可能漏了，加上后能正常可视化）
plt.show()