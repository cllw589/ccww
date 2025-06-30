import pandas as pd
import os

# 文件所在路径
file_path = r"F:\城市数据"

# 获取路径下所有符合条件的 CSV 文件
files = [f for f in os.listdir(file_path) if f.endswith('.csv')]

# 用于存储合并的数据
dfs = []
for file in files:
    # 读取每个 CSV 文件，注意根据实际编码和分隔符调整
    df = pd.read_csv(os.path.join(file_path, file), encoding='utf-8')
    # 提取年份，从文件名中截取，假设文件名如 “2015年国内主要城市年度数据.csv”
    year = file[:4]
    df['年份'] = year
    dfs.append(df)

# 1. 纵向连接合并数据
merged_df = pd.concat(dfs, ignore_index=True)

# 数据检查部分
print("===== 合并后数据基本情况检查 =====")
print("\n数据基本信息：")
merged_df.info()

# 查看数据集行数和列数
rows, columns = merged_df.shape

# 查看缺失值情况
print("\n各字段缺失值数量：")
print(merged_df.isnull().sum())

if rows < 5:
    # 行数少于5则打印全量数据信息
    print("\n数据全部内容信息：")
    print(merged_df.to_csv(sep='\t', na_rep='nan'))
else:
    # 行数多于5则打印数据前几行信息
    print("\n数据前几行内容信息：")
    print(merged_df.head().to_csv(sep='\t', na_rep='nan'))

# 2. 按照年份来聚合，3. 求每年的国内生产总值
# 先处理缺省值，填充为0
merged_df.fillna(0, inplace=True)
# 按年份聚合求国内生产总值总和
gdp_by_year = merged_df.groupby('年份')['国内生产总值'].sum()

print("\n===== 每年国内生产总值 =====")
print(gdp_by_year)