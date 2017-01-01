# -*- coding: utf-8 -*-
import requests

# baseHeaders = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
#     'Connection':'close'
# }

def postHtml(url,data,type):
    '''
    :param url:
    :param data:
    :return:html
    '''
    if type=='HX':
        response = requests.post(url, data=data)
        return response.json()['data']
    elif type=='PW':
        response=requests.post(url,data=data)
        return response.text



