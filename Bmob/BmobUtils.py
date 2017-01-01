# -*- coding: utf-8 -*-
import EveryBean
import requests
import demjson
#用于查询的URL
url='https://api.bmob.cn/1/classes/'
headers = {
        'Content-Type': 'application/json',
        'X-Bmob-Application-Id': '9e16e39fa5374f446e5c928da0f83d62',
        'X-Bmob-REST-API-Key': '42db163cd4c45884279b914e1c2a4e75'
    }

#用于删除表的URL
deleteUrl='https://api.bmob.cn/1/schemas/'
deleteHeaders={
    'X-Bmob-Application-Id': '9e16e39fa5374f446e5c928da0f83d62',
    'X-Bmob-Master-Key':'51ad9da949865e02ec6d6a044aef5436'
}

def encodeJson(str):
    '''
    将非json转化为JSON
    :param str:
    :return:
    '''
    return demjson.encode(str)


def decodeJson(json):
    '''
    将json转化为字符串
    :param json:
    :return:
    '''
    return demjson.decode(json)


def deleteBmobClass(className):
    '''
    清空某个表
    :param className:
    :return: responseCode
    '''
    allDeleteUrl=deleteUrl+className
    return requests.delete(allDeleteUrl,headers=deleteHeaders).text



def insertListBmob(className,list):
    '''
    把list<EveryBean>写入到bmob中
    :param className:
    :param list:
    :return: responseCode
    '''
    allUrl=url+className
    for item in list:
        data={}
        data['title']=item.getTitle()
        data['contentUrl'] = item.getContentUrl()
        data['imgUrl'] = item.getImgUrl()
        json=encodeJson(data)
        print(requests.post(allUrl, headers=headers,data=json).text)


def insertContentBmob(className,list):
    '''
    把list<EveryBean>写入到bmob中
    :param className:
    :param list:
    :return: responseCode
    '''
    allUrl=url+className
    for item in list:
        data={}
        data['url']=item.getContentUrl()
        data['contentHtml'] = item.getContentHtml()
        json=encodeJson(data)
        print(requests.post(allUrl, headers=headers,data=json).text)

