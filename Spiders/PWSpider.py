# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from HtmlUtils import HtmlGetUtils,HtmlPostUtils
from ListHtmlSpider import PWHtmlDealUtils
from ContentSpider import ContentHtmlSpider


class PW:
    def startSpider(self):
        '''
        针对品玩网的爬虫
        :return:
        '''
        #首先删除表
        # BmobUtils.deleteBmobClass("PWBean")


        for i in range(1,11):
            dataList=self.PWSecondListSpider(i)
            # contentList = ContentHtmlSpider.getContentIndex(dataList, 'WX')
            BmobUtils.insertListBmob('PWBean', dataList)
            # BmobUtils.insertContentBmob('PWContentBean', contentList)
            print("经过不懈的努力，开哥爬下了品玩科技第 %d 页" % i)


    def PWSecondListSpider(self,index):
        '''
        品玩网爬虫
        :param url:
        :return: List<PWBean>
        '''
        url2='http://www.pingwest.com/wp-admin/admin-ajax.php'
        data={
            'action':'my_ajax_allpost_next',
            'paged':index
        }

        html= HtmlPostUtils.postHtml(url2,data=data,type='PW')
        # print(html)
        datalist = PWHtmlDealUtils.dealFirstHtml(html)
        return datalist



