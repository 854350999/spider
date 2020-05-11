import json
import requests
import datetime
import simplejson
import time
import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', db='jisulife', charset='utf8mb4')
cursor = db.cursor()
sql_insert = 'INSERT INTO youpin(youpin_time, youpin_name, content, youpin_star) VALUES (%s,%s,%s,%s)'
for j in range(1, 51):

    postUrl = 'https://www.xiaomiyoupin.com/mtop/market/comment/product/content'
    # payloadData数据
    payloadData = {
        'folding': False,
        'gid': 112825,
        'pindex': j,
        'psize': 10,
        'source': 'PC',
        'tag_id': 0,
        'tag_name': '全部'
    }
    # 请求头设置
    payloadHeader = {
        'Host': 'www.xiaomiyoupin.com',
        'Content-Type': 'application/json',
        'cookie': 'youpindistinct_id=16eb0a525c76a9-082581b4e757d2-3a65420e; mjclient=PC; youpindistinct_id=16eb0a'
                  '525c76a9-082581b4e757d2-3a65420e; mjclient=PC; youpin_sessionid=1576043327482_16ef380affa6e8-00'
                  'aaebdd96c88f-3a65420e; Hm_lvt_025702dcecee57b18ed6fb366754c1b8=1575438544,1575438611,1576035248,'
                  '1576043328; youpin_sessionid=16ef7db6f4d-0f36bb62eb23b9-1f11; Hm_lpvt_025702dcecee57b18ed6fb3667'
                  '54c1b8=1576116384',
        'referer': 'https://www.xiaomiyoupin.com/detail?gid=112825&spmref=YouPinPC.$undefined$.search_list.3.93905513'
    }
    # 下载超时
    timeOut = 25
    # 代理

    r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
    dumpJsonData = json.dumps(payloadData)
    print(f"dumpJsonData = {dumpJsonData}")
    res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut, allow_redirects=True)
    print(f"responseTime = {datetime.datetime.now()}, statusCode = {res.status_code}, res text = {res.text}")
    response = res.text
    review = simplejson.loads(response)
    for i in range(0, 10):
        #爬取评论时间
        yp_time = review['data']['list'][i]['ctime']
        timeArray = time.localtime(yp_time)
        #爬取评论者昵称
        nick_name = review['data']['list'][i]['nick_name']
        #爬取小米有品评论
        content = review['data']['list'][i]['txt']
        #爬取评论星级
        star = review['data']['list'][i]['score']
        cursor.execute(sql_insert, (timeArray, nick_name, content, star))
        db.commit()
    time.sleep(10)
        # print(content)
db.close()