# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from HtmlUtils import HtmlGetUtils
from ListHtmlSpider import TSMCHtmlDealUtils
import time


class TSMC:
    def startSpider(self):
        '''
        针对硅谷密探的爬虫
        :return:
        '''
        #首先删除表
        # BmobUtils.deleteBmobClass("GGBean")


        for i in range(0,11):
            dataList=self.TSMCListSpider(i)
            BmobUtils.insertListBmob('TSMCBean', dataList)
            print("经过不懈的努力，开哥爬下了TSMC新闻第 %d 页" % i)


    def TSMCListSpider(self,index):
        '''
        硅谷密探网爬虫
        :param url:
        :return: List<PWBean>
        '''
        pn=20*index
        # print(pn)
        url = 'http://m.news.baidu.com/news'
        params={
            'tn':'bdapinewsearch',
            'word':u'台积电',
            'pn':'0',
            'rn':'20',
            'ct':'1'
        }
        params['pn']=pn

        html= HtmlGetUtils.getHtml(url,params=params)
        # print(html)
        datalist = TSMCHtmlDealUtils.dealHtml(html)
        return datalist



