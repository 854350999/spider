# -*- coding: utf8 -*-
import requests
import simplejson
import json
import csv
import time
import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', db='jisulife', charset='utf8mb4')
cursor = db.cursor()
sql_insert = 'INSERT INTO taobao(tb_date,tb_name,tb_productcolor,tb_content,tb_addcontent,tb_score) ' \
             'VALUES (%s, %s, %s, %s, %s, %s)'

base_url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=592961771418&userNumId=2744906942' \
           '&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0'
header = {'Connection': 'keep-alive',
          'Cookie': 't=33c30a88ace981db73a5ab2181d0e461; cna=pxlmFtGQ+yoCAXFmpAM7BpWg; uc3=id2=UUphzpYqX5cXz4y8lQ%3D'
                    '%3D&nk2=F5RDLjy6p5kZXRnW&lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dByuQGE%2FwCsoXSjuE%3D; lgc=tb62157425'
                    '58; uc4=id4=0%40U2grFbWxeDPEmc0F057GUPxb6XdamTOO&nk4=0%40FY4I7WLlGHTv%2FDuByUGgKVBhuAmC%2BGc%3D;'
                    ' tracknick=tb6215742558; _cc_=UIHiLt3xSw%3D%3D; tg=0; enc=4X4BkFOVbk3%2FPKZshupurD5ag0bxeX%2B0Kn'
                    'mgVVmbOJP%2F396LrfoX8wKioP0ITre723ai3Qxx1BswSq94LeG00g%3D%3D; miid=765165961011055585; cookie2=1'
                    '089d2e2b7fafd9e75f7bd31e14da440; _tb_token_=385b1ee763876; v=0; _m_h5_tk=73583f3d6710ca7fcb69e3e'
                    '597e2b151_1575521621094; _m_h5_tk_enc=7cda029311c62c98376c211462c2b78f; mt=ci=-1_0; thw=cn; hng'
                    '=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTbmE4XahSNBQ%3D%3D; x5sec=7b22726174656d616e616765723b32'
                    '223a226639626633636466633366306433343733366131316366303038373366356165435054746f653846454a6e517'
                    'a5962333659547862513d3d227d; l=dBS7fLLrq97UuaGaBOfZhurza77TUKAf5sPzaNbMiICP_3XdfTZGWZKOKgx9CnGV'
                    '3sNe83Jt3efYB0LZpyznhEGfIqlBs2JwQdTeR; isg=BHd3Cze15qZiamIdg2GTbaP4BmvBPEuegNoTfcksyceBeJ660g8'
                    'A788eWpiDkCMW',
          'Referer': 'https://item.taobao.com/item.htm?ut_sk=1.WykiL6wooO0DALv5Od%2Bd72eW_21380790_1575512891028.Din'
                     'gTalk.1&id=592961771418&sourceType=item&price=23-108&origin_price=46-216&suid=2FDF0605-6382-43F6'
                     '-8766-50668EF20CDC&un=fa747ccc2525ce11d707d2abce2ca380&share_crt_v=1&cpp=1&shareurl=true&spm=a'
                     '313p.22.zg.1089765288814&short_name=h.eDnPo2d&app=chrome',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/75.0.3770.100 Safari/537.36'}




for i in range(1,100,1):
    url = base_url + '&currentPageNum=%s' % str(i)

   # 将响应内容的文本取出
    tb_req = requests.get(url, headers=header).text[3:-2]
    print(tb_req)
   #将str格式的文本格式化为字典
    tb_dict = simplejson.loads(tb_req)
   #编码： 将字典内容转化为json格式对象
    tb_json = json.dumps(tb_dict, indent=2)   #indent参数为缩紧，这样打印出来是树形json结构，方便直观
   #解码： 将json格式字符串转化为python对象
    review_j = json.loads(tb_json)
    for p in range(0, 20, 1):
        zp = [review_j["comments"][p]['appendList']]
        pl = [review_j["comments"][p]['content'].encode('utf-8').decode('utf-8')]
        ys = [review_j["comments"][p]['auction']['sku'].encode('utf-8').decode('utf-8')]
        dat = [review_j["comments"][p]['date'].encode('utf-8').decode('utf-8')]
        name = [review_j["comments"][p]['user']['nick'].encode('utf-8').decode('utf-8')]
        sc = [review_j["comments"][p]['rate'].encode('utf-8').decode('utf-8')]
        if zp == [[]]:
            zp = None
        else:
            zp = [review_j["comments"][p]['appendList'][0]['content'].encode('utf-8').decode('utf-8')]
        cursor.execute(sql_insert, (dat, name, ys, pl, zp, sc))
        db.commit()
    time.sleep(5)
print('Done!')

