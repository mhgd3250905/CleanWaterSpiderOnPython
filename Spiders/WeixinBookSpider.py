# -*- coding: utf-8 -*-



from HtmlUtils import HtmlGetUtils
import time
import requests
from ListHtmlSpider import WXBookHtmlDealUtils
from Bmob import BmobUtils



#http://weixin.sogou.com/wapindex/wap/0612/wap_9/0.html

class WXBook:

    def startSpider(self):
        '''
        微信资讯爬虫统筹地
        :return:
        '''
        #清空一下数据表
        # BmobUtils.deleteBmobClass('WeixinBean')

        # headers={
        #     'Accept':'*/*',
        #     'Accept-Encoding':'gzip,deflate,sdch',
        #     'Accept-Language':'zh-CN,zh;q=0.8',
        #     'X-Requested-With':'XMLHttpRequest'
        # }

        #开始爬
        for i in range(1,11):

            url='http://weixin.sogou.com/remind/doc_list_openid.php'

            headers={
                'X-Requested-With':'XMLHttpRequest',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                # 'Cookie': 'ABTEST=8|1482679837|v1; SUID=E0E141DE232C940A00000000585FE61D; SUV=0059271B68C7C8D2585FE626CC329973; weixinIndexVisited=1; usid=UQpw5p7nuXEb1aDv; SUID=E0E141DE290B940A0000000058625B93; ppinf=5|1482841014|1484050614|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1NDolRTglQjclOUYlRTclOUQlODAlRTQlQkElOTElRTUlQTUlOTQlRTglQjclOTElRTMlODAlODJ8Y3J0OjEwOjE0ODI4NDEwMTR8cmVmbmljazo1NDolRTglQjclOUYlRTclOUQlODAlRTQlQkElOTElRTUlQTUlOTQlRTglQjclOTElRTMlODAlODJ8dXNlcmlkOjQ0OjhCMzE4QTk0N0EwOTk3RTgyRDU1RjM2NzlEMTlCMjVBQHFxLnNvaHUuY29tfA; pprdig=VxxcJTe3khwuXwNWYH4yoNY3MiVmbjwOItZGbSVnptmDDsbD_Q92KtTCVuUdITvGNn4ER2gt6BHutLoUndHrVs1hLRoCHnaBKjofkdecggNWEwuV70PrKMctmUab6Xe2dhpccFIEmWcoUcamsdDKc0ImrrkzArjh98BUSSHCHjY; SNUID=4A40F7DE696C2C5B77BED78F6A51F1A5; ppmdig=148345215600000072910a2fca5b4f0dad63f7eeaece4388; IPLOC=CN3100; JSESSIONID=aaaScgBgSLeHcd85vu7Kv; sct=31',
                # 'Referer':'http://weixin.sogou.com/home'

            }

            params={

                'from': 'web',
                'uid': '8B318A947A0997E82D55F3679D19B25A@qq.sohu.com',
                'openidid': '',
                'start': '0',
                'num': '10',
                'clear': '1',
                '_': '1483453318728',
            }

            # cookies={
            #     'Cookie':'ABTEST=8|1482679837|v1; SUID=E0E141DE232C940A00000000585FE61D; SUV=0059271B68C7C8D2585FE626CC329973; weixinIndexVisited=1; usid=UQpw5p7nuXEb1aDv; SUID=E0E141DE290B940A0000000058625B93; ppinf=5|1482841014|1484050614|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1NDolRTglQjclOUYlRTclOUQlODAlRTQlQkElOTElRTUlQTUlOTQlRTglQjclOTElRTMlODAlODJ8Y3J0OjEwOjE0ODI4NDEwMTR8cmVmbmljazo1NDolRTglQjclOUYlRTclOUQlODAlRTQlQkElOTElRTUlQTUlOTQlRTglQjclOTElRTMlODAlODJ8dXNlcmlkOjQ0OjhCMzE4QTk0N0EwOTk3RTgyRDU1RjM2NzlEMTlCMjVBQHFxLnNvaHUuY29tfA; pprdig=VxxcJTe3khwuXwNWYH4yoNY3MiVmbjwOItZGbSVnptmDDsbD_Q92KtTCVuUdITvGNn4ER2gt6BHutLoUndHrVs1hLRoCHnaBKjofkdecggNWEwuV70PrKMctmUab6Xe2dhpccFIEmWcoUcamsdDKc0ImrrkzArjh98BUSSHCHjY; SNUID=4A40F7DE696C2C5B77BED78F6A51F1A5; ppmdig=148345215600000072910a2fca5b4f0dad63f7eeaece4388; IPLOC=CN3100; JSESSIONID=aaaScgBgSLeHcd85vu7Kv; sct=31'
            # }

            params['_']='%d' % (1000*(time.time()))

            response= requests.get(url,headers=headers,params=params)
            # print(response.text)

            datalist= WXBookHtmlDealUtils.dealHtml(response.text)
            # contentList=ContentHtmlSpider.getContentIndex(datalist,'WX')
            BmobUtils.insertListBmob('WXBookBean', datalist)
            # # BmobUtils.insertContentBmob('WeixinContentBean',contentList)
            print("经过不懈的努力，开哥爬下了微信订阅号第 %d 页" % i)

