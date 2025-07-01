import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 设置图片清晰度和大小
plt.rcParams['figure.dpi'] = 200
plt.figure(figsize=(12, 5))

# 尝试多种中文字体，提高兼容性
plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC', 'Source Han Sans SC']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 读取数据集
try:
    df = pd.read_csv(r"F:\exercise_data\train.csv")

except FileNotFoundError:
    print(f"错误：找不到文件 F:\\exercise_data\\train.csv，请检查文件路径是否正确。")
    exit()
except Exception as e:
    print(f"读取数据时发生错误：{e}")
    exit()

# 确保数据中包含所需的列
required_columns = ['Age', 'Survived']
if not all(col in df.columns for col in required_columns):
    missing_cols = [col for col in required_columns if col not in df.columns]
    print(f"错误：数据集中缺少以下列：{missing_cols}，无法进行分析。")
    exit()

# 处理年龄缺失值（使用中位数填充）
df['Age'] = df['Age'].fillna(df['Age'].median())

# 1. 年龄分布直方图（整体）
plt.subplot(1, 2, 1)
sns.histplot(df['Age'], kde=True, color='skyblue', bins=np.arange(0, 81, 10))
plt.title('整体年龄分布（0-80岁，间隔10岁）')
plt.xlabel('年龄')
plt.ylabel('频数')
plt.xlim(0, 80)  # 设置x轴范围

# 2. 不同生还状态的年龄分布对比
plt.subplot(1, 2, 2)
sns.histplot(df, x='Age', hue='Survived', kde=True,
             palette=['lightblue', 'salmon'],
             bins=np.arange(0, 81, 10),
             common_norm=False)
plt.title('不同生还状态的年龄分布对比（0-80岁，间隔10岁）')
plt.xlabel('年龄')
plt.ylabel('频数')
plt.xlim(0, 80)  # 设置x轴范围
plt.legend(['未生还', '生还'])

# 调整x轴刻度为10的倍数
for ax in plt.gcf().axes:
    ax.set_xticks(np.arange(0, 81, 10))

# 调整子图布局
plt.tight_layout()
plt.show()