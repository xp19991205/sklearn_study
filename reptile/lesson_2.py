import requests

key_word = input("请输入一个关键词")
param = {
    'query': key_word
}
headers = {
    'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
}
#第一步：指定url
url = "https://www.sougou.com/web"
#第二步：发起请求
responce = requests.get(url= url, params=param,headers = headers)
#get方法会返回一个响应对象
#第三步：获取响应数据
page_text = responce.text #获取到网页的源码数据
print(page_text)
filename = key_word +".html"
file_path = "./"+filename
#持久化存储
with open(file_path,'w',encoding='utf-8') as fp:
    fp.write(page_text)

#出现的问题就是多来几次这个就被拒绝了
