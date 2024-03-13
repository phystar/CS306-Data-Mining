import pandas as pd

# 读取CSV文件
df = pd.read_csv('Reviews.csv')

# 记录去重前的数据长度
len_before = len(df)

# 删除重复的行
df = df.drop_duplicates()

# 记录去重后的数据长度
len_after = len(df)

# 计算并打印保留数据的百分比
percentage_retained = (len_after / len_before) * 100
print(f"Percentage of data retained after deduplication: {percentage_retained}%")