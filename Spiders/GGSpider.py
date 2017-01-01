# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from HtmlUtils import HtmlPostUtils
from ListHtmlSpider import GGHtmlDealUtils
import time


class GG:
    def startSpider(self):
        '''
        针对硅谷密探的爬虫
        :return:
        '''
        #首先删除表
        # BmobUtils.deleteBmobClass("GGBean")


        for i in range(1,11):
            dataList=self.GGListSpider(i)
            BmobUtils.insertListBmob('GGBean', dataList)
            print("经过不懈的努力，开哥爬下了品玩科技第 %d 页" % i)


    def GGListSpider(self,index):
        '''
        硅谷密探网爬虫
        :param url:
        :return: List<PWBean>
        '''
        url = 'http://www.svinsight.com/api?callback=jQuery111306490858093306913_%d' % (time.time() * 1000)

        data = {
            'id': '208',
            'query': '''{"global": {"Loc": 2, "OS": 2, "Port": 300, "Sign": "", "Token": ""},
                           "data": {"Index":%d, "OrderBy": 0, "QueryString": [], "Size": 1}}''' % index
        }

        html= HtmlPostUtils.postHtml(url,data=data,type='PW')
        # print(html)
        datalist = GGHtmlDealUtils.dealHtml(html)
        return datalist



