import requests
from bs4 import BeautifulSoup


def crawl_douban_top10():
    # 定义爬取网址
    url = "https://movie.douban.com/chart"

    # 定义浏览器表头信息，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        # 向目标网站发送请求并获取网页源码
        rs = requests.get(url, headers=headers, timeout=10)
        print(f"响应状态: {rs.status_code}")

        # 检查请求是否成功
        if rs.status_code != 200:
            print(f"请求失败，状态码: {rs.status_code}")
            return []

        # 使用BeautifulSoup解析网页
        soup = BeautifulSoup(rs.text, 'html.parser')

        # 定位包含电影条目的<tr>标签
        movie_list = []
        for idx, tr in enumerate(soup.select('tr.item')):
            if idx >= 10:  # 只取前10部电影
                break

            # 提取电影标题（包含在<div class="pl2">的<a>标签内）
            title_div = tr.find('div', class_='pl2')
            if title_div:
                title_link = title_div.find('a')
                if title_link:
                    # 获取标题文本并清除额外空格和换行符
                    title = title_link.get_text(strip=True)
                    # 去除标题中不需要的副标题部分（如果存在）
                    if '/' in title:
                        title = title.split('/')[0].strip()
                    movie_list.append(title)

        return movie_list

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")
        return []
    except Exception as e:
        print(f"解析发生错误: {e}")
        return []


if __name__ == "__main__":
    top10_movies = crawl_douban_top10()

    if not top10_movies:
        print("未能获取电影列表")
    else:
        print("\n豆瓣一周口碑榜 TOP10:")
        for i, title in enumerate(top10_movies, 1):
            print(f"{i}. {title}")