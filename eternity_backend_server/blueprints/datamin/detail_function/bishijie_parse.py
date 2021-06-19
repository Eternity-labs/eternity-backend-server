from bs4 import BeautifulSoup
from lxml import etree
import json

# xpath需要定期更换，否则数据抓取不全

def  bishijie_info_parse(parse_str:str = ''):
    """
    传入一个待解析的字符串
    """
    # html_info = etree.HTML(parse_str,parser=None)
    soup = BeautifulSoup(parse_str,features="lxml")
    info_list = soup.find_all('div',class_="content")
    result_info_list = []
    for info in info_list:
        title = info.find('h3').text.replace('\n','').replace(' ','')
        content = info.find('div',class_='h63').text.replace('\n','').replace(' ','')
        look_count_true = info.find('div',class_='bull').text.replace('\n','').replace(' ','')
        look_count_flase = info.find('div',class_='bear').text.replace('\n','').replace(' ','')
        result_info_list.append({"title":title,
                                 "content":content,
                                 "look_count_true":look_count_true,
                                 "look_count_flase":look_count_flase})
    result_info = {
        "status":True,
        "info":"bishijie Fetch results",
        "info_list":result_info_list
    }
    return result_info