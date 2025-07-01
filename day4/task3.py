import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 设置图片清晰度和大小（减小图片尺寸）
plt.rcParams['figure.dpi'] = 200  # 降低DPI
plt.figure(figsize=(8, 5))  # 减小画布尺寸

# 尝试多种中文字体，提高兼容性
plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC', 'Source Han Sans SC']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 读取数据集（使用双反斜杠或原始字符串）
try:
    # 方法1：使用双反斜杠
    # df = pd.read_csv("F:\\exercise_data\\train.csv")

    # 方法2：使用原始字符串（推荐）
    df = pd.read_csv(r"F:\exercise_data\train.csv")

    # 检查数据基本信息
    print("数据基本信息：")
    df.info()

    # 查看数据集行数和列数
    rows, columns = df.shape

    if rows < 100 and columns < 20:
        # 短表数据（行数少于100且列数少于20）查看全量数据
        print("数据全部内容：")
        print(df.to_csv(sep='\t', na_rep='nan'))
    else:
        # 长表数据查看数据前几行
        print("数据前几行内容：")
        print(df.head().to_csv(sep='\t', na_rep='nan'))

except FileNotFoundError:
    print(f"错误：找不到文件 F:\\exercise_data\\train.csv，请检查文件路径是否正确。")
    exit()
except Exception as e:
    print(f"读取数据时发生错误：{e}")
    exit()

# 确保数据中包含所需的列
required_columns = ['Pclass', 'Survived']
if not all(col in df.columns for col in required_columns):
    missing_cols = [col for col in required_columns if col not in df.columns]
    print(f"错误：数据集中缺少以下列：{missing_cols}，无法进行分析。")
    exit()

# 计算每个乘客等级的生还率
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean().reset_index()
survival_rate_by_class.columns = ['乘客等级', '生还率']

# 打印每个乘客等级的生还率
print("\n每个乘客等级的生还率：")
print(survival_rate_by_class)

# 绘制直方图展示乘客等级对生还率的影响
# sns.barplot(x='乘客等级', y='生还率', data=survival_rate_by_class, zorder=3)
sns.barplot(x='乘客等级', y='生还率', data=survival_rate_by_class, color='skyblue', zorder=3)  # 指定颜色

# 添加标题和标签
plt.title('乘客等级对生还率的影响')
plt.xlabel('乘客等级')
plt.ylabel('生还率')
plt.ylim(0, 1)  # 设置y轴范围为0到1，更直观展示生还率

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

# 调整边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

# 调整刻度标签
plt.xticks(rotation=45, ha='right')

# 在每个柱子上显示具体的生还率数值
for i, rate in enumerate(survival_rate_by_class['生还率']):
    plt.text(i, rate + 0.02, f'{rate:.2f}', ha='center', fontweight='bold')

# 显示图形
plt.tight_layout()
plt.show()