import requests
import lxml.html
import pandas as pd
import pymysql
import random
import time
def get_response(ASIN, p, headers):
    url = 'https://www.amazon.com/dp/product-reviews/' + str(ASIN) +'/ref=cm_cr_arp_d_paging_btm_prev_13?ie=UTF8&reviewerType=all_reviews&sortBy=recent' + '&pageNumber=%s'%str(p)
    html = requests.get(url, headers=headers, timeout=8).text
    response = lxml.html.fromstring(html)
    return response
def Spider(response, j):
    info = []
    new_date = response.xpath('//*[@id="cm_cr-review_list"]/div[%s]/div[1]/div[1]/span/text()' % str(j))
    # 爬取评论者名称
    new_name = response.xpath(
        '//*[@id="cm_cr-review_list"]/div[%s]/div[1]/div[1]/div[1]/a/div[2]/span/text()' % str(j))
    # 爬取评论星级
    new_star = \
        response.xpath('//*[@id="cm_cr-review_list"]/div[%s]/div[1]/div[1]/div[2]/a/i/span/text()' % str(j))[0]
    # 爬取评论者购买size
    new_size = response.xpath('//*[@id="cm_cr-review_list"]/div[%s]/div[1]/div[1]/div[3]/a/text()' % str(j))
    # 爬取评论者购买颜色分类
    new_color = response.xpath('//*[@id="cm_cr-review_list"]/div[%s]/div[1]/div[1]/div[3]/a/text()[2]' % str(j))
    # 匹配评论者评论
    new_content = response.xpath('//*[@id="cm_cr-review_list"]/div[%s]/div[1]/div[1]/div[4]/span/span/text()' % str(j))
    # print(new_size, new_color)
    if len(new_name) == 0:
        new_name = response.xpath('//*[@id="cm_cr-review_list"]/'
                                  'div[%s]/div[1]/div[1]/div[1]/div[1]/div[1]/a/div[2]/span/text()' % str(j))
    if len(new_color) == 0:
        new_color = new_size
        new_size = [None]
    info.append([new_date, new_name, new_color, new_size, new_star, new_content])
    return info
def save_mysql(info, ASIN):
    db = pymysql.connect(host='localhost', user='root', password='root', db='jisulife', charset='utf8mb4')
    cursor = db.cursor()
    sql_insert = 'INSERT INTO amazon_reviews(ASIN, A_date,A_name,A_size, A_color, A_star,A_content) ' \
                 'VALUES (%s, %s, %s,%s,  %s, %s, %s)'
    new_info = info[0]
    cursor.execute(sql_insert,
                   (ASIN, new_info[0], new_info[1], new_info[2], new_info[3],new_info[4], new_info[5]))
    db.commit()
    db.close()
if __name__ == '__main__':
    ASIN_list = pd.read_excel('E:\\WT\\project\\data\\ASIN.xls')['ASIN']
    cookie_list = pd.read_excel('E:\\WT\\project\\data\\cookie.xls')['cookie']
    cookie = random.choice(cookie_list)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                             '49.0.2623.112 Safari/537.36',
               'cookie': cookie
               }
    for i in range(0, len(ASIN_list)):
        ASIN = ASIN_list[i]
        try:
            # 亚马逊评论页数最多500页
            for p in range(0, 500):
                res = get_response(ASIN, p, headers)
                for j in range(1, 11):
                    info = Spider(res, j)
                    save_mysql(info, ASIN)
            time.sleep(random.uniform(3, 5))
        except:
            pass

