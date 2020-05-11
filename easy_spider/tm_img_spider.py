# -*- coding: utf8 -*-
from urllib import request
import requests
import pandas
import urllib
import re
import sys
import importlib
importlib.reload(sys)
url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.6410a98at7nPDn&q=%BC%D3%CA%AA%C6%F7' \
      '&sort=d&style=g&from=mallfp..pc_1_searchbutton&active=2'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/65.0.3325.181 Safari/537.36',
            'cookie':'cna=0kOrFaL8SSUCAXFmp1DP3o33; UM_distinctid=16bd5efeeb9278-02b543ea415f2f-3a614f0b-1fa400-16bd5ef'
                     'eeba16b; lid=tao%E5%B0%8A%E8%80%85; enc=rXV4Bsk%2FnHjArh7WxnIrYZru8MkmhUuD7GlKBSwl1dX%2F7%2Bx9k'
                     'quIskaSm%2Bw6ufBK98YarsOU31xPhVa21ylOFg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; otherx=e%3D1%26p%3D'
                     '*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; cq=ccp%3'
                     'D1; _uab_collina=156325668167138887123048; tk_trace=1; t=ea1628b1aed74387d3d3f986f3739198; uc'
                     '3=lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=F5fTBwT53Q%3D%3D&id2=UUtNgbl4jRwokQ%3D%3D&vt3=F8dBy3zVyr%2Brqj'
                     'WSAck%3D; tracknick=tao%5Cu5C0A%5Cu8005; lgc=tao%5Cu5C0A%5Cu8005; _tb_token_=3bffee37bee79; co'
                     'okie2=7f63b033fd59099130efe2bbca31d90d; tt=jx.tmall.com; _m_h5_tk=78e09b92ffb3ecd5e39ed66f9e11'
                     'fe6a_1564719338944; _m_h5_tk_enc=afe5fbe52ec68ce518c58da60313913b; res=scroll%3A1903*5496-clien'
                     't%3A1903*943-offset%3A1903*5496-screen%3A1920*1080; pnm_cku822=098%23E1hvd9vUvbpvUvCkvvvvvjiPRF'
                     'Fw1jrWR2dOgjD2PmPZljDEPL5UQjtEPszh1jnm2QhvCvvvMM%2FtvpvIphvvvvvvphCvpCQmvvC2qhCvjvUvvhBGphvwv9'
                     'vvBHBvpCQmvvChx8yCvv3vpvo18UnTpOyCvvXmp99hVtIEvpCWBC9Yv8WKnpxsBOD1K33spAxtlwmXeABgnpcWsEIKnpxs'
                     'BIx1K33spcyDlwmXekpVfvDrs8TJOyC%2Bm7zhditQcmx%2FQj7JVVQHNZsv1vhCvvXvppvvvvvtvpvhphvvv8wCvvBvpv'
                     'pZ; l=cB_B2lsHqx_dw31CKOCwNuI8LKQTGIRAguPRwCvpi_5CU6Yd6bbOkSvJHFv6cjWd9KLB4IQ3Fvp9-etkiepTY-c'
                     'HtBUV.; isg=BPz8DwpUjcxF1Ll305G0AJn3zZpuXaEtn-b2GNZ9ZOfDoZwr_gMgrlIThYl86dh3',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'path': '/search_product.htm?q=%CA%D6%B3%D6%D0%A1%B7%E7%C9%C8&type=p&vmarket=&spm=a2156.1676643.a222'
                    '7oh.d100&from=mallfp..pc_1_searchbutton',
            'referer': 'https://list.tmall.com/search_product.htm?q=%BC%D3%CA%AA%C6%F7&type=p&vmarket=&spm'
                       '=a2156.1676643.a2227oh.d100&from=mallfp..pc_1_searchbutton'}
html = requests.request('GET', url, headers=header).text
    # ren = re.compile('"title":"(.*?)","pic_url":"(.*?)","price":"(.*?)","importantKey":"(.*?)","month_sales":"(.*?)"')
#ren = re.findall('data-nick="(.*?)"', html)#天猫店铺名
#ren1 = re.findall('title="(.*?)"><b>', html)#天猫价格（需清洗）
#ren2 = re.findall(r'(.*?)笔', html)#天猫销量
ren3 = re.findall('img  data-ks-lazyload=  "(.*?)"', html)
ren4 = re.findall('img  src=  "(.*?)"', html)
print(ren3)
print(ren4)
ren5 = ren4 + ren3
print(ren5)
    #data = re.findall(ren, html)
    # print data
#data2 = pandas.DataFrame(ren)
#data3 = pandas.DataFrame(ren1)
#data4 = pandas.DataFrame(ren2)
#data2 = pandas.DataFrame(ren3)
#print(data2)
#print(data3)
#print(data4)
#data4.to_csv(r'tianmao5.csv', header=False, index=False, mode='a+',encoding='utf-8')
#data2.to_csv(r'tianmao5.csv', header=False, index=False, mode='a+',encoding='utf-8')
#data3.to_csv(r'tianmao5.csv', header=False, index=False, mode='a+',encoding='utf-8')
#print(html[667:])

#print(data)
#print(data2)
#for i in range(0, 50, 1):
    #this_img_url = "http:"+ren3[i]
    #print(this_img_url)
    #img_path = "E:\\WT\\project\\taobao_img\\" + str(i) + ".jpg"
    #urllib.request.urlretrieve(this_img_url, img_path)