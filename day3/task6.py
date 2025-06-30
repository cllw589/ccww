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

# 纵向连接合并数据
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

# 处理缺省值，填充为0
merged_df.fillna(0, inplace=True)

# 按年份聚合求国内生产总值总和
gdp_by_year = merged_df.groupby('年份')['国内生产总值'].sum()

print("\n===== 每年国内生产总值 =====")
print(gdp_by_year)

# 5. 计算每个城市2015-2017年GDP的年均增长率，并找出增长率最高和最低的五个城市
# 筛选2015-2017年数据
years_2015_2017 = merged_df[merged_df['年份'].isin(['2015', '2016', '2017'])]

# 计算每个城市的年均增长率
def calculate_growth_rate(city_data):
    # 获取2015年和2017年的GDP
    gdp_2015 = city_data[city_data['年份'] == '2015']['国内生产总值'].values[0]
    gdp_2017 = city_data[city_data['年份'] == '2017']['国内生产总值'].values[0]
    # 计算年均增长率: (V_end/V_start)^(1/n)-1，n=2表示2年
    return ((gdp_2017 / gdp_2015) ** 0.5 - 1) * 100  # 转换为百分比

# 按"地区"分组并计算增长率
city_growth_rates = years_2015_2017.groupby('地区').apply(calculate_growth_rate).reset_index(name='年均增长率(%)')

# 找出增长率最高和最低的五个城市
top_five_cities = city_growth_rates.sort_values('年均增长率(%)', ascending=False).head(5)
bottom_five_cities = city_growth_rates.sort_values('年均增长率(%)').head(5)

print("\n===== 年均GDP增长率最高的五个城市 =====")
print(top_five_cities)
print("\n===== 年均GDP增长率最低的五个城市 =====")
print(bottom_five_cities)

# 6. 对医院、卫生院数进行归一化处理（Min-Max标准化），并按年份比较各城市医疗资源的变化
# 假设数据中存在"医院、卫生院数"列，如果列名不同请修改
hospitals = merged_df[['年份', '地区', '医院、卫生院数']].copy()

# 按年份进行Min-Max标准化
def min_max_normalize(group):
    group['医院、卫生院数(标准化)'] = (group['医院、卫生院数'] - group['医院、卫生院数'].min()) / \
                                  (group['医院、卫生院数'].max() - group['医院、卫生院数'].min())
    return group

normalized_hospitals = hospitals.groupby('年份').apply(min_max_normalize)

print("\n===== 医院、卫生院数归一化结果 =====")
print(normalized_hospitals)

# 7. 提取北京、上海、广州、深圳四个城市2015-2017的GDP和社会商品零售总额数据，用新的csv呈现
selected_cities = ['北京', '上海', '广州', '深圳']  # 根据实际数据中的城市名称可能需要调整
selected_data = merged_df[
    (merged_df['年份'].isin(['2015', '2016', '2017'])) &
    (merged_df['地区'].isin(selected_cities))
][['年份', '地区', '国内生产总值', '社会商品零售总额']]  # 根据实际列名可能需要调整

# 保存到新的CSV文件
output_path = r"F:\城市数据\北上广深经济数据_2015-2017.csv"
selected_data.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"\n===== 已将北上广深2015-2017年数据保存到 {output_path} =====")