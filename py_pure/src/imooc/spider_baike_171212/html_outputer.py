class HtmlOutputer:
    def __init__(self):
        self.datas = []

    def collect_data(self, data):  # 收集爬取到的数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):  # 将爬取到的数据写到本地
        with open('log/output.html', 'w', encoding='utf-8') as f:
            f.write("<html>")
            f.write("<meta charset='utf-8'/> ")
            f.write("<body>")
            f.write("<table>")

            count = 1
            print('datas-->',self.datas)
            for data in self.datas:
                print('data-->', data)
                f.write("<tr>")
                # f.write("<td>%s</td>" % str(data['url'].encode('utf-8'), 'utf-8'))
                # f.write("<td>%s</td>" % str(data['title'].encode('utf-8'), 'utf-8'))
                # f.write("<td>%s</td>" % str(data['summary'].encode('utf-8'), 'utf-8'))
                f.write("<h1>%s(%s)</h1>" % (str(data['title'].encode('utf-8'), 'utf-8'), count))
                f.write("<p><font size=6>%s</font></p>" % str(data['summary'].encode('utf-8'), 'utf-8'))
                f.write("</tr>")
                count += 1

            f.write("</table>")
            f.write("</body>")
            f.write("</html>")
