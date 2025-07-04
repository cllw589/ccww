# 实训日志
## 一、爬虫基础初探  
今日首次接触 Python 爬虫实战，尝试爬取电影网站信息及学术文献链接。过程中发现 Python 生态中蕴藏着丰富的爬虫工具：  
- **爬虫库**：如 `requests` 可便捷发送网络请求，`BeautifulSoup` 能高效解析 HTML 结构；  
- **模拟人类行为库**：`Selenium` 配合浏览器驱动，可模拟鼠标点击、滚动等操作，解决动态页面爬取难题。  


## 二、数据处理与可视化核心库学习  
### 1. pandas：数据处理 
- **核心功能**：专注于数据框（DataFrame）格式运算，支持读取、清洗、转换 `excel`、`csv` 等格式文件；  
- **实操场景**：通过 `pandas` 对爬取的电影数据进行去重、排序及字段提取，瞬间将杂乱数据整理成结构化表格，效率提升显著。  

### 2. matplotlib：数据可视化 
- **核心能力**：将抽象数据转化为直观图表，支持条形图、折线图、散点图等多种可视化形式；  
- **案例实践**：用 `matplotlib` 绘制电影评分分布直方图，通过调整 `color`、`label`、`xticks` 等参数，让数据趋势以 “图像化” 方式清晰呈现。  

## 三、学习感悟与展望  
今日学习从数据抓取到处理分析形成了完整闭环：爬虫库解决 “数据从哪来”，`pandas` 解决 “数据如何处理”，`matplotlib` 解决 “数据如何呈现”。