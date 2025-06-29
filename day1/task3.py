# 任务1：列表推导式筛选偶数
numbers = [x for x in range(1, 101)]
even_numbers = [x for x in numbers if x % 2 == 0]
print("1-100的偶数：", even_numbers)

# 任务2：列表去重保持顺序
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

sample_list = [3, 1, 2, 2, 4, 3, 5, 1]
print("\n原始列表：", sample_list)
print("去重后列表：", remove_duplicates(sample_list))

# 任务3：合并两个列表为字典
keys = ["a", "b", "c"]
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print("\n合并后的字典：", merged_dict)

# 任务4：元组解包学生信息
student = ("张三", 20, 90)
name, age, score = student
print("\n学生信息解包：")
print(f"姓名：{name}, 年龄：{age}, 成绩：{score}")