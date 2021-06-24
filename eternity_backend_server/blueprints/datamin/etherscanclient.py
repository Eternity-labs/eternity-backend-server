import requests
import logging
from eternity_backend_server import settings
import re
from bs4 import BeautifulSoup
from lxml import etree
import time
from eternity_backend_server.blueprints.datamin.detail_function import token_parse
import json


class etherscanclient(object):
    """
    数据采集入口类
    """

    def __init__(self, token, apikey):
        self.token = token
        self.apikey = apikey

    def contractaddress(self):
        '''
        https://api-cn.etherscan.com/api?module=stats&action=tokensupply&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&apikey=YourApiKeyToken
        '''
        return json.loads(datamin_contractaddress(self.token, self.apikey))

    def tokencontractaddress(self):
        '''
        https://api-cn.etherscan.com/api?module=account&action=tokenbalance&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&address=0xe04f27eb70e025b78871a2ad7eabe85e61212761&tag=latest&apikey=YourApiKeyToken
        '''
        return json.loads(datamin_tokencontractaddress(self.token, self.apikey))

    def token_info(self):
        '''
        https://cn.etherscan.com/token/0x358AA737e033F34df7c54306960a38d09AaBd523
        '''
        return json.loads(datamin_token_info(self.token))

    def token_transfers(self):
        '''
        https://cn.etherscan.com/token/generic-tokentxns2?contractAddress=0x358AA737e033F34df7c54306960a38d09AaBd523&mode=&sid=4632ba89ca08b23ff97da5d8c6f47cb2&m=normal&p=2
        '''
        return datamin_token_transfers(self.token)


def datamin_token_info(
    contractaddress:str = "0x358AA737e033F34df7c54306960a38d09AaBd523"
    ):
    """
    抓取token当中的部分内容
    """
    headers = settings.HEADERS_TOKEN
    url = 'https://cn.etherscan.com/token/{}'.format(contractaddress)
    response = requests.get(url=url, headers=headers)
    base_info = token_parse.overview_info_parse(response.text)
    return base_info

def datamin_token_transfers(
    contractaddress:str = "0x358AA737e033F34df7c54306960a38d09AaBd523"
    ):
    """
    抓取token当中的Transfers内容 
    """
    headers = settings.HEADERS_TOKEN
    url = 'https://cn.etherscan.com/token/{}'.format(contractaddress)
    response = requests.get(url=url, headers=headers)
    try:
        sid = re.findall(r"sid = '(.*?)';",response.text)[0] # 获取sid码
        url = 'https://cn.etherscan.com/token/generic-tokentxns2?m=normal&contractAddress={}&a=&sid={}&p=1'.format(contractaddress,sid)
        response = requests.get(url=url, headers=headers)
        # ==========获取页数===========
        html_info = etree.HTML(response.text,parser=None)
        page_count = int(html_info.xpath('string(//*[@id="maindiv"]/div[2]/div/div/ul/li[3]/span/strong[2])'))
        # ==========获取页数结束========
        info_list = []
        for page_info in range(1,page_count+1):
            url = 'https://cn.etherscan.com/token/generic-tokentxns2?m=normal&contractAddress={}&a=&sid={}&p={}'.format(contractaddress,sid,page_info)
            response = requests.get(url=url, headers=headers)
            pe_page_list = token_parse.overview_info_transfers_parse(response.text)
            info_list.append({str(page_info):pe_page_list})
            time.sleep(0.4)
        dict_info = {'status':True,
                     'info_list':info_list}
        return dict_info
    except:
        overview_info = "sid parsing failed"
        return overview_info



def datamin_contractaddress(
    contractaddress:str = "0x358AA737e033F34df7c54306960a38d09AaBd523",
    apikey:str = ''
    ) ->str:
    """
    docstring
    """
    try:
        headers = settings.HEADERS_API
        params = (
            ('module', 'stats'),
            ('action', 'tokensupply'),
            ('contractaddress', contractaddress),
            ('apikey', apikey),
        )
        response = requests.get('https://api-cn.etherscan.com/api', headers=headers, params=params)
        return response.text
    except Exception as e:
        logging.warning('请求失败，失败类型为：%s'%e)
        return '请求失败，失败类型为：%s'%e
# TokenContractAddress
def datamin_tokencontractaddress(
    contractaddress:str = "0x358AA737e033F34df7c54306960a38d09AaBd523",
    apikey:str = ''
    ) ->str:
    """
    docstring
    """
    try:
        headers = settings.HEADERS_API
        params = (
        ('module', 'account'),
        ('action', 'tokenbalance'),
        ('contractaddress', contractaddress),
        ('address', '0xe04f27eb70e025b78871a2ad7eabe85e61212761'),
        ('tag', 'latest'),
        ('apikey', apikey)
        )
        response = requests.get('https://api-cn.etherscan.com/api', headers=headers, params=params)
        return response.text

    except Exception as e:
        logging.warning('请求失败，失败类型为：%s'%e)
        return '请求失败，失败类型为：%s'%e