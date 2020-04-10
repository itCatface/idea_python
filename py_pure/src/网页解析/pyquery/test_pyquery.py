from pyquery import PyQuery as pq

with open('../用于测试解析的网页.html', 'r', encoding='utf-8', errors='ignore') as f:
    doc = pq(f.read())

# css选择器-选择标签名则不需加任何标记 | id前加# | class前加.
print("doc('li'): ", doc('li'))
print("doc('#container'): ", doc('#container'))
print("doc('.list'): ", doc('.list'))

# 查找id为container class为list标签为a的对象
print("doc('#container .list a'): ", doc('#container .list a'))

# 子元素
print("doc('.list').find('li'): ", doc('.list').find('li'))

# 使用.children()查找直接子元素
print("doc('.list').children(): ", doc('.list').children())

print("doc('.list').children('.active'): ", doc('.list').children('.active'))

# .parent()父节点
print("doc('.list').parent: ", doc('.list').parent())

# .parents()祖先节点
print("doc('.list').parents(): ", doc('.list').parents())
print("doc('li').parents('container'): ", doc('li').parents('list'))

# .siblings()兄弟节点
print("doc('.list .item-0.active').siblings(): ", doc('.list .item-0.active').siblings())

# 遍历
lis = doc('li').items()
for li in lis:
    print('遍历li标签: ', li)

# 获取信息
print("doc('.item-0.active a').attr('href'): ", doc('.item-0.active a').attr('href'))
print("doc('.item-0.active a').attr.href: ", doc('.item-0.active a').attr.href)

# 获取文本
print("doc('.item-0.active a').text(): ", doc('.item-0.active a').text())

# 获取html
print("doc('.item-0.active').html(): ", doc('.item-0.active').html())

# DOM操作
li = doc('.item-0.active')
print("doc('.item-0.active'): ", li)
li.remove_class('active')
print("li.remove_class('active'): ", li)
li.add_class('active')
print("li.add_class('active'): ", li)

# attr css
li = doc('.item-0.active')
print("doc('.item-0.active'): ", li)
li.attr('name', 'link')
print("li.attr('name', 'link'): ", li)
li.css('font-size', '14px')
print("li.css('font-size', '14px'): ", li)

# 伪类选择器
print("doc('li:first-child'): ", doc('li:first-child'))
print("doc('li:last-child'): ", doc('li:last-child'))
print("doc('li:nth-child(2)'): ", doc('li:nth-child(2)'))
print("doc('li:gt(2)[选择前3个之后的所有元素]'): ", doc('li:gt(2)'))
print("doc('li:nth-child(2n)'): ", doc('li:nth-child(2n)'))
print("doc('li:contains(second)'): ", doc('li:contains(second)'))

# remove
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
    <a href='www.baidu.com'>百度一下</a>
</div>
'''

doc = pq(html)
wrap = doc('.wrap')
print("doc('.wrap').text(): ", doc('.wrap').text())
doc('.wrap').find('p').remove()
doc('.wrap').find('a').remove()
print("p.remove() & a.remove(): ", wrap.text())
