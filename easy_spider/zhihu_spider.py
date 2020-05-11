# -*- coding: utf8 -*-
import requests
import simplejson
import json
import numpy as np
import string
import csv
import time
import pymysql

url1 = 'https://www.zhihu.com/api/v4/search_v3?t=general&q=%E7%A8%8B%E5%BA%8F%E5%91%98&correction=1' \
       '&offset=20&limit=20&lc_idx=25&show_all_topics=0&search_hash_id=ee640a9529bdab69dd2f5aad9bc3eece' \
       '&vertical_info=0%2C1%2C0%2C1%2C0%2C0%2C0%2C0%2C0%2C1'
header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.344'
                  '0.106 Safari/537.36',
}
#知乎url的后面部分
hz = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapse' \
                  'd%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Cs' \
                  'uggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Cres' \
                  'hipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant' \
                  '_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2' \
                  'Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.ma' \
                  'rk_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&o' \
                  'ffset=5&platform=desktop&sort_by=default'
print(type(hz))
tb_req = requests.get(url1, headers=header).text
# print(tb_req)
# 将str格式的文本格式化为字典
print(tb_req)
# print(len(tb_req))
tb_dict = simplejson.loads(tb_req)
# 编码： 将字典内容转化为json格式对象
tb_json = json.dumps(tb_dict, indent=2)  # indent参数为缩紧，这样打印出来是树形json结构，方便直观
# 解码： 将json格式字符串转化为python对象
review_j = json.loads(tb_json)
for p in range(0, 19, 1):
    ys = [review_j["data"][p]['object']['url'].encode('utf-8').decode('utf-8')]
    if "answers" in str(ys):
        wz = [review_j["data"][p]['object']['question']['url'].encode('utf-8').decode('utf-8')]
        #调整得出的网址前面部分格式
        wz1 = str(wz).strip('[')
        wz2 = str(wz1).strip(']')
        wz3 = eval(str(wz2).replace("api", "www"))
        wz4 = wz3.replace("com/", "com/api/v4/")
        wz5 = str(wz4)+hz
        print(wz5)
print('Done')
tb = requests.get(wz5, headers=header).text
print(tb)