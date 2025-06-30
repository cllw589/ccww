import requests
from lxml import etree
import os
from urllib.parse import urljoin


def download_images():
    # 目标网址
    url = "http://pic.netbian.com/"

    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Referer': url
    }

    try:
        # 1. 创建保存图片的目录（如果不存在）
        save_dir = 'd:\\images\\'
        os.makedirs(save_dir, exist_ok=True)  # 创建目录（如果已存在则忽略）
        print(f"图片将保存到: {os.path.abspath(save_dir)}")

        # 2. 请求网页并设置编码
        response = requests.get(url, headers=headers)
        response.encoding = "gbk"  # 该网站使用GBK编码
        response.raise_for_status()  # 检查HTTP错误

        # 3. 解析HTML
        html = etree.HTML(response.text)

        # 更精确的XPath定位：查找所有列表中的图片
        img_elements = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
        print(f"找到 {len(img_elements)} 张图片")

        # 4. 遍历并下载图片
        for i, img_path in enumerate(img_elements, 1):
            # 使用urljoin正确处理相对路径
            img_url = urljoin(url, img_path)

            try:
                # 获取图片响应
                img_response = requests.get(img_url, headers=headers, stream=True)
                img_response.raise_for_status()

                # 确定文件名和扩展名
                original_name = os.path.basename(img_path)
                file_ext = os.path.splitext(original_name)[1] or '.jpg'  # 保留原始扩展名
                filename = f"{i}-{original_name}" if original_name else f"image-{i}{file_ext}"

                # 保存路径
                save_path = os.path.join(save_dir, filename)

                # 以二进制写入图片
                with open(save_path, 'wb') as f:
                    # 使用chunk写入避免大文件占用内存
                    for chunk in img_response.iter_content(chunk_size=8192):
                        if chunk:  # 过滤keep-alive新块
                            f.write(chunk)

                print(f"✅ 成功下载: {filename} (大小: {os.path.getsize(save_path) // 1024}KB)")

            except Exception as img_err:
                print(f"⚠️ 下载图片失败: {img_url}, 原因: {img_err}")

        print("\n====== 图片下载完成 ======")

    except requests.exceptions.RequestException as req_err:
        print(f"🔴 网络请求失败: {req_err}")
    except Exception as e:
        print(f"🔴 程序运行出错: {e}")
    finally:
        print("任务结束")


if __name__ == "__main__":
    download_images()