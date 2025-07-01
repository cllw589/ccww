import numpy as np
import matplotlib.pyplot as plt

# 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数
gold_medal = np.array([16, 12, 9, 8, 8])
# 银牌个数
silver_medal = np.array([8, 10, 4, 10, 5])
# 铜牌个数
bronze_medal = np.array([13, 5, 2, 7, 5])

# 生成 x 轴坐标，数量与国家列表长度一致
x = np.arange(len(countries))

# 恢复 x 轴的坐标，将国家名称作为 x 轴刻度显示
plt.xticks(x, countries)

# 绘制金牌柱状图，调整位置和颜色
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold", label='金牌')
# 绘制银牌柱状图
plt.bar(x, silver_medal, width=0.2, color="silver", label='银牌')
# 绘制铜牌柱状图
plt.bar(x + 0.2, bronze_medal, width=0.2, color="saddlebrown", label='铜牌')

# 定义添加文本标签的通用函数，避免重复代码
def add_text_labels(x_pos, medal_data, offset):
    for i in range(len(x_pos)):
        plt.text(x_pos[i] + offset, medal_data[i], medal_data[i],
                 va='bottom', ha='center', fontsize=8)

# 给金牌添加文本标签，偏移量 -0.2
add_text_labels(x, gold_medal, -0.2)
# 给银牌添加文本标签，偏移量 0
add_text_labels(x, silver_medal, 0)
# 给铜牌添加文本标签，偏移量 +0.2
add_text_labels(x, bronze_medal, 0.2)

# 添加图例，展示不同颜色柱状图代表的含义
plt.legend()
# 显示绘制的图表
plt.show()