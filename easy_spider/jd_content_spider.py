# -*- coding: utf8 -*-
import requests
import simplejson
import json
import time
import pymysql
import random


db = pymysql.connect(host='localhost', user='root', password='root', db='jisulife', charset='utf8mb4')
cursor = db.cursor()
sql_insert = 'INSERT INTO jingdongc' \
             '(jd_date,jd_name,jd_productcolor,jd_content,jd_appcontent,jd_score) ' \
             'VALUES (%s, %s, %s, %s, %s, %s)'
base_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv56' \
           '&productId=3973338&score=0&sortType=6&pageSize=10&isShadowSku=0&fold=1'
header = {'Connection': 'keep-alive',
          'Cookie': '__jdu=1829136083; areaId=19; ipLoc-djd=19-1607-40152-0; shshshfpa=f06ef28e-713d-3d6f-5645-37'
                    '82f5064e15-1571735789; shshshfpb=p1v9nDVk8Ux7F8esDcIxHKg%3D%3D; unpl=V2_ZzNtbUEEFhYhC0EEchkP'
                    'B2IKFggRAxcTdw1OASsdCQFmCkYKclRCFX0URlVnGl4UZwoZXkdcQRJFCEdkexhdBWAEFlRDUXMlRQtGZHopXAxkCxJfR'
                    'VZKF0U4QVRyKWzT6I3F%2b9aB1bWis%2fdkexBeBmQAE19DUXMURQhPUXgQWgxmBBptCTlCWHUBRVx7G1sEbgEiWEJVRx'
                    'N0C0VkeA%3d%3d; __jdv=76161171|www.hkdgl.cn|t_1001665807_|tuiguang|2bd2e26a81b3485dbee7349da5'
                    'd508ef|1571826277361; __jda=122270672.1829136083.1571735785.1571826277.1571887465.5; __jdb=12'
                    '2270672.1.1829136083|5.1571887465; __jdc=122270672; shshshfp=35e5c2b6e8e44e01b525bbfc39701ab3'
                    '; shshshsID=7320216c35f7d68bed520899feb8e7e1_1_1571887466019; 3AB9D23F7A4B3C9B=2G36J3IZSL3W6SJ'
                    'YZB3K4NSTBBV4R3VXXQEYSIELCWFDR2B46PD7MQSHK42N7UBC6MDUNIAIXU2C5JPHVA4LLHQ7WM; JSESSIONID=245810'
                    '1700380A1D588E634FD53BF725.s1',
          'Referer': 'https://item.jd.com/3973338.html'}




for i in range(21,100,1):
    url = base_url + '&page=%s' % str(i)
   # 将响应内容的文本取出
    tb_req = requests.get(url, headers=header).text[24:-2]
   #print(tb_req)
   #将str格式的文本格式化为字典
    print(tb_req)
    tb_dict = simplejson.loads(tb_req)
   #编码： 将字典内容转化为json格式对象
    tb_json = json.dumps(tb_dict, indent=3)   #indent参数为缩紧，这样打印出来是树形json结构，方便直观
   #解码： 将json格式字符串转化为python对象
    review_j = json.loads(tb_json)
    for p in range(0, 10, 1):
        pl = [review_j["comments"][p]['content'].encode('utf-8').decode('utf-8')]
        sc = [review_j["comments"][p]['score']]
        ys = [review_j["comments"][p]['productColor'].encode('utf-8').decode('utf-8')]
        name = [review_j["comments"][p]['nickname'].encode('utf-8').decode('utf-8')]
        dat = [review_j["comments"][p]['creationTime'].encode('utf-8').decode('utf-8')]
        zp = [review_j["comments"][p]['afterDays']]
        if zp == [0]:
            zp = None
        else:
            zp = [review_j["comments"][p]['afterUserComment']
                  ['hAfterUserComment']['content'].encode('utf-8').decode('utf-8')]
        cursor.execute(sql_insert, (dat, name, ys, pl, zp, sc))
        db.commit()
    time.sleep(random.uniform(2.5, 5))
print('Done!')

