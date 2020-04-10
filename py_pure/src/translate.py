def fanyi_word_cn(string):
    url="https://fanyi.so.com/index/search"
    #db_path = './db/tasks.db'
    Form_Data= {}

    #这里输入要翻译的英文
    Form_Data['query']= string
    Form_Data['eng']= '1'

    #用urlencode把字典变成字符串，#服务器不接受字典，只接受字符串和二进制
    data= parse.urlencode(Form_Data).encode('utf-8')

    #改成服务器可识别的数据后，请求，获取回应数据
    response= request.urlopen(url, data)

    html= response.read().decode("utf-8")#解码方式

    #java中的对象（集合）和数组（元素为集合）,loads可转Python字典
    result= json.loads(html)

    #字典调取键名data下的键名fanyi,获取其值
    translate_result= result["data"]["fanyi"]
    #print(translate_result)
    return translate_result