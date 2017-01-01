# -*- coding: utf-8 -*-
import requests
from io import BytesIO
import gzip

baseHeaders = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    'Connection':'close'
}


def byteToString(byteData):
    '''
    将byte转化为String
    :param byteData:
    :return: String
    '''
    return BytesIO(byteData).read().decode()

#获取目标Html

def getHtml(url,params=0,headers=0):
    '''
    传入URL 返回Html字符串
    :param url:
    :return: String
    '''
    if params!=0:
        if headers==0:
            #如果参数params不为零那么说明来自泡泡网
            return requests.get(url,headers=baseHeaders,params=params).text
        else:
            mergedHeaders=dict(baseHeaders, **headers)
            return requests.get(url,headers=mergedHeaders,params=params).text
    else:
        if headers==0:
            #否则来自哔哩哔哩或者微信
            return requests.get(url,headers=headers).text
        else:
            mergedHeaders=dict(baseHeaders, **headers)
            response=requests.get(url, headers=mergedHeaders)
            # return response.text
            if response.headers['Content-Encoding']=='gzip':
                result=BytesIO(response.content).read().decode()
                return result
            else:
                return response.text







