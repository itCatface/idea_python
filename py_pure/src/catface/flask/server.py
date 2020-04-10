import os
from os import path

from flask import Flask, request, json, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

default_json = '{"code":"0","data":{"userInfo":{"opId":"20180210","rsp":"0","orgId":"4007250"},"password":"测试get-pass","busiInfo":[{"busiName":"套餐0","busiId":"taocan0","id":"0"},{"busiName":"套餐1","busiId":"taocan1","id":"1"}],"username":"测试get-name"},"message":"操作成功"}';


@app.route('/')
def hello_world():
    return 'Hello Flask!'


@app.route("/test/test_get", methods=['get'])
def test_get():
    print("test/test_get")
    return default_json


@app.route("/test/test_get_", methods=['get'])
def test_get_():
    name = request.args.get('name')
    passd = request.args.get('pass')
    print("test/test_get_" + name + " || " + passd)
    return default_json


@app.route("/test/test_post", methods=['post'])
def test_post():
    print("test/test_post")
    return default_json


@app.route("/test/test_post_", methods=['post'])
def test_post_():
    name = request.form['name']
    passd = request.form['pass']
    print("test/test_post_" + name + " || " + passd)
    return default_json


@app.route("/test/test_put", methods=['put'])
def test_put():
    print("test/test_put")
    return default_json


@app.route("/test/test_put_", methods=['put'])
def test_put_():
    name = request.form.get('name')
    passd = request.form.get('pass')
    print("test/test_put_" + name + " || " + passd)
    return default_json


@app.route("/test/test_delete_/<id>", methods=['delete'])
def test_delete_(id):
    print("test/test_delete_" + id)
    return default_json


@app.route("/test/test_json_", methods=['post'])
def test_json_():
    json = request.get_data().decode('utf-8')
    print("test/test_json_" + json)
    return json


@app.route("/test/test_upload", methods=['post'])
def test_upload():
    try:
        print(request.files)
        f1 = request.files["file1"]
        f2 = request.files["file2"]
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path, 'static/uploads/')
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        f1.save(upload_path + f1.filename)
        f2.save(upload_path + f2.filename)
    except Exception as e:
        return "文件上传错误", e
    return "文件上传成功"


@app.route("/test/test_download", methods=['get'])
def test_download():
    dir = "D:\projects\idea\idea_learn_web\sbt_test\download/"
    filename = request.args.get('filename')
    if not filename:
        return "请添加需要下载的文件名..."
    else:
        return send_from_directory(dir, filename, as_attachment=True)


# # # # # # #
draw_json = ""

if __name__ == '__main__':
    app.run(debug=True,
            host='127.0.0.2',
            port=8088
            )  # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
