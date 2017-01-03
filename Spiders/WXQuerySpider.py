# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from HtmlUtils import HtmlGetUtils
import time
import requests
from ListHtmlSpider import PythonHtmlDealUtils


class WXQuery:
    def __init__(self,keyWord,beanName):
        self.keyWord=keyWord
        self.beanName=beanName

    def startSpider(self):
        '''
        针对吴亦凡的爬虫
        :return:
        '''
        #首先删除表
        # BmobUtils.deleteBmobClass("GGBean")


        for i in range(1,11):
            dataList=self.PythonListSpider(i,self.keyWord)
            BmobUtils.insertListBmob(self.beanName, dataList)
            print("经过不懈的努力，开哥爬下了微信python第 %d 页" % i)


    def PythonListSpider(self,index,keyWord):
        '''
        硅谷密探网爬虫
        :param url:
        :return: List<PWBean>
        '''
        pn=20*index
        # print(pn)
        url = 'http://weixin.sogou.com/weixinwap?'
        params={
            'page':'0',
            '_rtype':'json',
            'ie':'utf8',
            'type':'2',
            't':'1482843684884',#这个是时间戳
            'query':'Python',#这个是关键词
            'pg':'webSearchList',
            '_sug_':'n',
            '_sug_type_':'',
            '':''
        }

        params['query']=keyWord
        params['page']='%d' % index
        params['t']='%d' %(time.time()*1000)

        responseJson=requests.get(url=url,headers=HtmlGetUtils.baseHeaders,params=params).content
        responseJsonEncode=HtmlGetUtils.byteToString(responseJson)
        print(responseJsonEncode)

        datalist = PythonHtmlDealUtils.dealHtml(responseJsonEncode)
        return datalist



