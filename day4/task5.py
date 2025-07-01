import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 全局配置：优化字体、分辨率
plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
try:
    df = pd.read_csv(r"F:\exercise_data\train.csv")
except FileNotFoundError:
    print("错误：文件路径不正确或文件不存在，请检查！")
    exit()

# 数据预处理：填充年龄缺失值
df['Age'] = df['Age'].fillna(df['Age'].median())

# 创建 2 行 2 列子图，合理分配画布空间
fig, axes = plt.subplots(2, 2, figsize=(12, 10), gridspec_kw={'wspace': 0.3, 'hspace': 0.4})

# ------------------------- 1. 按性别分组的年龄分布对比 -------------------------
sns.histplot(
    df, x='Age', hue='Sex', kde=True,
    palette=['#4682B4', '#F08080'],  # 蓝色（男）、粉色（女）
    bins=np.arange(0, 81, 10), common_norm=False,
    ax=axes[0, 0]
)
axes[0, 0].set_title('1. 按性别分组的年龄分布对比', fontsize=12)
axes[0, 0].set_xlabel('年龄', fontsize=10)
axes[0, 0].set_ylabel('频数', fontsize=10)
axes[0, 0].set_xlim(0, 80)
axes[0, 0].legend(['男性', '女性'], title='性别', title_fontsize=10, fontsize=9)

# --------------------- 2. 按性别 + 生还状态分组的年龄分布 ---------------------
# 构造组合分组字段
df['Sex_Survived'] = df['Sex'] + '_' + df['Survived'].astype(str)

sns.histplot(
    df, x='Age', hue='Sex_Survived', kde=True,
    palette={'male_0': '#B0C4DE', 'male_1': '#1E3A5F',
             'female_0': '#FFC0CB', 'female_1': '#B22222'},
    bins=np.arange(0, 81, 10), common_norm=False,
    ax=axes[0, 1]
)
axes[0, 1].set_title('2. 按性别 + 生还状态分组的年龄分布', fontsize=12)
axes[0, 1].set_xlabel('年龄', fontsize=10)
axes[0, 1].set_ylabel('频数', fontsize=10)
axes[0, 1].set_xlim(0, 80)
axes[0, 1].legend(
    ['男性-未生还', '男性-生还', '女性-未生还', '女性-生还'],
    title='分组', title_fontsize=10, fontsize=9
)

# ------------------- 3. 按性别 + 年龄组的生还率对比（分组柱状图） -------------------
# 划分年龄组
df['AgeGroup'] = pd.cut(
    df['Age'], bins=np.arange(0, 91, 10),
    labels=['0-10岁', '10-20岁', '20-30岁', '30-40岁',
            '40-50岁', '50-60岁', '60-70岁', '70-80岁', '80-90岁']
)

# 计算生还率
survival_rate = df.groupby(['Sex', 'AgeGroup'])['Survived'].mean().reset_index()

sns.barplot(
    data=survival_rate, x='AgeGroup', y='Survived', hue='Sex',
    palette=['#4682B4', '#F08080'], ax=axes[1, 0]
)
axes[1, 0].set_title('3. 按性别 + 年龄组的生还率对比', fontsize=12)
axes[1, 0].set_xlabel('年龄组', fontsize=10)
axes[1, 0].set_ylabel('生还率', fontsize=10)
axes[1, 0].set_ylim(0, 1)
axes[1, 0].tick_params(axis='x', rotation=45)  # 旋转 x 轴标签
axes[1, 0].legend(['男性', '女性'], title='性别', title_fontsize=10, fontsize=9)

# 标注生还率数值
for container in axes[1, 0].containers:
    axes[1, 0].bar_label(container, fmt='%.2f', fontsize=8, padding=3)

# --------------------- 4. 性别 + 年龄 对生还率的联合分布（核密度图） ---------------------
sns.kdeplot(
    data=df, x='Age', y='Survived', hue='Sex',
    fill=True, common_norm=False, alpha=.5,
    palette=['#4682B4', '#F08080'],
    ax=axes[1, 1]
)
axes[1, 1].set_title('4. 性别 + 年龄 对生还率的联合分布', fontsize=12)
axes[1, 1].set_xlabel('年龄', fontsize=10)
axes[1, 1].set_ylabel('生还率', fontsize=10)
axes[1, 1].legend(['男性', '女性'], title='性别', title_fontsize=10, fontsize=9)

# 整体布局优化
plt.suptitle('性别与年龄对生还率的影响分析', fontsize=14, y=0.95)
plt.show()