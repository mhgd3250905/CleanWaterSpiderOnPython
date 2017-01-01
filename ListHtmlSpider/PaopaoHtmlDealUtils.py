# -*- coding: utf-8 -*-
import re
from EveryBean import Bean

# 返回DataBeanList
def dealHtml(html):
    '''
    接收传入的Html字符串，处理之后返回List（PaopaoBean）
    分析使用的是正则表达式
    :param html:
    :return: biliList
    '''
    paopaoList=[]
    #获取每一个Item
    items=re.findall(r"\{\"ID\".+?\}",html)
    print(len(items))
    #对每一个item中进行分析 提取出title/contentUrl/imgUrl 并加入到list中
    for item in items:
        title=re.findall(r"\"F_ArtTitle\":\"(.*?)\",",item)
        imageUrl = re.findall(r"\"F_PicSrc\":\"(.*?)\",",item)
        contentUrl = re.findall(r"\"ArtLink\":\"(.*?)\",", item)

        print(title[0])
        print(imageUrl[0])
        print(contentUrl[0])
        bean = Bean.DataBean(title[0],contentUrl[0], imageUrl[0])
        paopaoList.append(bean)
        print('==================================================================')



    return paopaoList