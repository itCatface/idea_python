# -requests[第三方库可代替内建的urllib库用于访问网络]
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.douban.com/'
r = requests.get(url, headers=headers)
print('status: %s\ncontent: %s' % (r.status_code, r.text))

r = requests.get(url, headers=headers, params={'q': 'python', 'cat': '1001'})
print('url-->', r.url)
print('text-->', r.text)
print('content-->', r.content)

# 直接抓取json
r = requests.get('https://wanandroid.com/wxarticle/chapters/json')
print('json-->', r.json())

# post请求
r = requests.post('https://accounts.douban.com/login', headers=headers, data={'form_email': 'abc@example.com', 'form_password': '123456'})
print('post-->', r.content)

# 上传文件
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)
