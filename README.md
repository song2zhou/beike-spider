### beike-spider

- 贝壳网房价数据爬虫，python新人练手项目

- 源自[lianjia-beike-spider](https://github.com/jumper2014/lianjia-beike-spider.git)，作了精简和改动

### 使用方法

- 安装python依赖环境`pip3 install -r requirements.txt`，国内环境可以指定软件源`pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/`

- 根目录下执行爬虫脚本`python3 beike_spider.py`，爬虫自动爬取`http://[city_name].fang.ke.com/loupan/`下的房价数据，并根据当前日期[data]保存到data/[city_name]/data/xxx.csv文件中

### TODO

- 交互指定[city_name]

- 纵向分析房价走势

- 自动开启脚本定时爬取房价数据，形成数据库

- 链家数据爬取