import requests
#第一步：指定url
url = "https://www.sogou.com/"
#第二步：发起请求
responce = requests.get(url= url)
#get方法会返回一个响应对象
#第三步：获取响应数据
page_text = responce.text #获取到网页的源码数据
#持久化存储
with open('./sougou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
