import pandas as pd

# 读取 CSV 文件，注意路径转义，这里使用原始字符串或者双反斜杠
df = pd.read_csv(r"F:\exercise_data\drinks.csv")
print("数据基本信息：")
df.info()

# 查看数据集行数和列数
rows, columns = df.shape
if rows < 5:
    # 行数少于5则打印全量数据信息
    print("数据全部内容信息：")
    print(df.to_csv(sep='\t', na_rep='nan'))
else:
    # 行数多于5则打印数据前几行信息
    print("数据前几行内容信息：")
    print(df.head().to_csv(sep='\t', na_rep='nan'))
# 1. 哪个大陆(continent)平均消耗的啤酒(beer_servings)更多？
beer_mean_by_continent = df.groupby('continent')['beer_servings'].mean()
continent_with_most_beer = beer_mean_by_continent.idxmax()
print(f"平均消耗啤酒最多的大陆是：{continent_with_most_beer}")

# 2. 打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
wine_describe_by_continent = df.groupby('continent')['wine_servings'].describe()
print("每个大陆红酒消耗的描述性统计值：")
print(wine_describe_by_continent)

# 3. 打印出每个大陆每种酒类别的消耗平均值
mean_by_continent_and_drink = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].mean()
print("每个大陆每种酒类别的消耗平均值：")
print(mean_by_continent_and_drink)

# 4. 打印出每个大陆每种酒类别的消耗中位数
median_by_continent_and_drink = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].median()
print("每个大陆每种酒类别的消耗中位数：")
print(median_by_continent_and_drink)