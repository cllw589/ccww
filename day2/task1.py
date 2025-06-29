# 1. 判断回文数
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# 2. 计算平均值
def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

# 3. 返回最长字符串
def find_longest_string(*strings):
    return max(strings, key=len) if strings else ""

# 4. 矩形计算（面积和周长）
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# 测试示例
if __name__ == "__main__":
    print(f"121 是回文数: {is_palindrome(121)}")
    print(f"参数平均值: {calculate_average(1, 2, 3, 4)}")
    print(f"最长字符串: {find_longest_string('apple', 'banana', 'cherry')}")
    print(f"矩形面积: {rectangle_area(5, 3)}")
    print(f"矩形周长: {rectangle_perimeter(5, 3)}")