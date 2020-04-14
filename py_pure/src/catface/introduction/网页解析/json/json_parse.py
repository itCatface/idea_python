import json
import requests

# -dict和json转换
# 下面两种方式声明dict是一样的效果
json_dict = dict(name='ashe', age=17)
json_dict = {'name': 'ashe', 'age': 17}

# dumps()将dict对象转换为字符串
json_str = json.dumps(json_dict)
# eval()将字符串转换为dict
json_dict = eval(json_str)
# loads()将字符串转换为dict[json对象]
json_obj = json.loads(json_str)
print(type(json_dict), '--', json_dict, '||', json_dict['name'])
print(type(json_str), '--', json_str)
print(type(json_obj), '--', json_obj, '||', json_obj['name'])

# 使用案例1
json_dict = {'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 2, 'translateResult': [[{'src': 'test', 'tgt': '测试'}]]}
print('取dict中的某个字段值', json_dict['translateResult'][0][0]['tgt'])
print('取json(dict)中的某个字段值', json.loads(json.dumps(json_dict))['translateResult'][0][0]['tgt'])
# 使用案例2
json_str = '{"name":"ashe", "age":17}'
json_obj = json.loads(json_str)
print(json_str, '<--json_str && json_obj-->', json_obj, " || 取json字段值：", json_obj['name'])

# 使用案例3-直接获取接口返回的json
with requests.get(url='https://www.wanandroid.com/tree/json') as r:
    print('接口返回的完整json：', r.json())
    print('取json中某个字段值：', r.json()['data'][0]['children'][0]['name'])

# -读写json文件
# with open('temp.json', 'a', encoding='utf-8') as f:
#     f.write(json.dumps(json_str))

with open('temp.json', 'r') as f:
    data = json.load(f)
    print('data:', data)
