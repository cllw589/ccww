import os
import re

# 定义文件路径（请修改为实际路径）
name_file = r"F:\作业\姓名.txt"  # 姓名文本路径
image_folder = r"F:\作业\图片"  # 图片文件夹路径


def get_names_from_file(name_file):
    """从文本文件中按顺序获取姓名"""
    try:
        with open(name_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"读取姓名文件失败：{e}")
        return []


def natural_sort_key(s):
    """自定义自然排序键，实现与资源管理器一致的排序规则"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def get_image_files_in_order(folder):
    """按资源管理器显示顺序获取图片文件（从左到右）"""
    try:
        # 获取所有png文件
        image_files = [f for f in os.listdir(folder) if f.lower().endswith('.png')]
        if not image_files:
            print("警告：图片文件夹中未找到png文件")
            return []

        # 使用自定义排序键实现自然排序
        image_files.sort(key=natural_sort_key)
        return image_files
    except Exception as e:
        print(f"获取图片文件失败：{e}")
        return []


try:
    # 1. 读取姓名列表（从上到下）
    names = get_names_from_file(name_file)
    print(f"成功读取{len(names)}个姓名")

    # 2. 按显示顺序获取图片文件（从左到右）
    image_files = get_image_files_in_order(image_folder)
    print(f"从文件夹中获取到{len(image_files)}个png图片")

    # 3. 显示前5个文件用于验证顺序
    print("\n前5个姓名：", names[:5])
    print("前5个图片：", image_files[:5])
    input("\n请确认以上顺序是否匹配（按Enter继续，Ctrl+C取消）")

    # 4. 数量匹配检查
    min_count = min(len(names), len(image_files))
    if len(names) != len(image_files):
        print(f"⚠️ 注意：姓名数量({len(names)})与图片数量({len(image_files)})不匹配，仅处理前{min_count}个")

    # 5. 执行重命名
    renamed_count = 0
    for i in range(min_count):
        old_name = image_files[i]
        new_name = f"{names[i]}.png"
        old_path = os.path.join(image_folder, old_name)
        new_path = os.path.join(image_folder, new_name)

        # 安全检查
        if not os.path.exists(old_path):
            print(f"❗ 警告：文件{old_path}不存在，跳过")
            continue
        if os.path.exists(new_path):
            print(f"❗ 警告：文件{new_path}已存在，跳过")
            continue

        os.rename(old_path, new_path)
        print(f"✅ 已重命名：{old_name} → {new_name}")
        renamed_count += 1

    print(f"✨ 重命名完成，共成功处理{renamed_count}个文件")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 {name_file} 或 {image_folder}")
except PermissionError:
    print(f"❌ 错误：无权限修改文件，请检查文件夹权限")
except Exception as e:
    print(f"❌ 处理失败：{str(e)}")
