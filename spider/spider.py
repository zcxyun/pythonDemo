from urllib import request
import re


class Spider(object):
    url = "https://www.panda.tv/cate/kingglory"

    def __fetch_content(self):
        with request.urlopen(Spider.url) as r:
            self.__html = r.read().decode('utf-8')

    def __analysis(self):
        # 匹配标题
        # data = re.findall(
            # r'<span class="video-title".*?>(.*?)</span>.*?<span class="video-number".*?>(.*?)</span>', self.__html, re.S)
        # 匹配昵称
        data = re.findall(
            r'<span class="video-nickname" title="(.*?)">.*?<span class="video-number">(.*?)</span>', self.__html, re.S)
        sortedData = sorted(
            data, key=lambda x: float(x[1][:-1]) * 10000 if '万' in x[1] else float(x[1]), reverse=True)
        for i, [user, score] in enumerate(sortedData):
            print(i+1, user, '===============================', score)

    def show(self):
        self.__fetch_content()
        self.__analysis()


spider = Spider()
spider.show()
