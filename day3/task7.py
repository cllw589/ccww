import pandas as pd
import numpy as np

# 1. 创建包含数据的 DataFrame 并保存为 students.csv
data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', None, 'David', 'Ella'],  # Name 列包含 1 个空值
    'Score': [85, np.nan, 90, 88, 92],  # Score 列包含 1 个空值
    'Grade': ['A', 'B', 'A', 'B', 'A']
}
df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)  # 保存为 CSV 文件，不包含索引列

# 2. 读取 CSV 文件，打印前 3 行
df_read = pd.read_csv('students.csv')
print("前 3 行数据：")
print(df_read.head(3))

# 3. 填充缺失值（避免使用 inplace=True）
df_read['Name'] = df_read['Name'].fillna('Unknown')  # 直接赋值替代 inplace
score_mean = df_read['Score'].mean()
df_read['Score'] = df_read['Score'].fillna(score_mean)  # 直接赋值替代 inplace

# 4. 将处理后的 DataFrame 保存为新 CSV 文件 students_cleaned.csv
df_read.to_csv('students_cleaned.csv', index=False)
print("数据处理完成并保存为 students_cleaned.csv")