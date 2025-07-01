import pandas as pd
import matplotlib.pyplot as plt
import os

# 数据文件所在目录
data_dir = r"F:\城市数据"
# 年份列表，对应要读取的文件
years = [2015, 2016, 2017]
dfs = {}

# 1. 读取文件并查看列信息
for year in years:
    file_path = os.path.join(data_dir, f"{year}年国内主要城市年度数据.csv")
    # 读取 CSV 文件
    df = pd.read_csv(file_path)
    dfs[year] = df
    # 查看当前年份数据的列名
    print(f"{year}年数据的列名：{df.columns.tolist()}")
    # 查看当前年份数据的前 5 行，了解数据结构
    print(f"{year}年数据前 5 行：\n{df.head()}")
    print("-" * 50)

# 根据实际列名，确定城市列和 GDP 列
city_col = "地区"
gdp_col = "国内生产总值"

# 2. 绘制2015 - 2017年各个城市的国内生产总值的直方图，横坐标为城市
# 先将三年的数据合并，方便绘制分组直方图（也可分别绘制单年直方图，根据需求调整）
combined_df = pd.concat(dfs.values(), keys=years, names=["年份", "原索引"])
plt.figure(figsize=(12, 6))
for year in years:
    df = dfs[year]
    # 检查列是否存在（实际列名已确认，也可省略检查，不过保留更鲁棒 ）
    if city_col in df.columns and gdp_col in df.columns:
        # 调整柱子位置的偏移量，实现分组效果
        x = range(len(df[city_col]))
        offset = (year - min(years)) * 0.2
        plt.bar([i + offset for i in x], df[gdp_col], width=0.2, label=str(year))
    else:
        print(f"{year}年数据缺少必要列，无法绘制对应直方图部分")

if city_col in combined_df.columns:
    plt.xticks([i + 0.2 for i in range(len(combined_df[city_col].unique()))], combined_df[city_col].unique())
plt.xlabel("城市")
plt.ylabel("国内生产总值")
plt.title("2015 - 2017年各城市国内生产总值直方图")
plt.legend()
plt.show()

# 3. 绘制2015年各个城市的国内生产总值的饼状图
df_2015 = dfs[2015]
if city_col in df_2015.columns and gdp_col in df_2015.columns:
    plt.figure(figsize=(8, 8))
    plt.pie(df_2015[gdp_col], labels=df_2015[city_col], autopct="%1.1f%%")
    plt.title("2015年各城市国内生产总值饼状图")
    plt.show()
else:
    print("2015年数据缺少必要列，无法绘制饼状图")