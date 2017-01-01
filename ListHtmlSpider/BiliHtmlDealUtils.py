# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from EveryBean import Bean
# 返回DataBeanList
def dealHtml(html):
    '''
    处理html
    :param html:
    :return:返回Bilibili List
    '''
    biliList=[]

    soup=BeautifulSoup(html,'html.parser')
    # print(soup)
    for item in soup.find_all('a','list-item'):
        #获取标题
        title = item.find('div', 'r').find('div', 'title').text
        # print(title)
        # 获取内容链接
        contentUrl=item['href']
        # print(contentUrl)
        #获取图片链接
        imgUrl=item.find('div','l').find('div','cover')['data-img']
        # print(imgUrl)

        # 生成DataBean并加入到列表中
        biliBean=Bean.DataBean(title, contentUrl, imgUrl)
        biliList.append(biliBean)

    # print("这一页的资源有 %d 条，现在开始爬虫！" % len(biliList))

    return biliList