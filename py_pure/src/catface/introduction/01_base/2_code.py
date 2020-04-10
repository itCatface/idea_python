# -字符编码
ord_a = ord('a')
ord_chinese = ord('王')
chr_123 = chr(97)
chr_27387 = chr(20000)
print('ord_a:', ord_a, ' | ord_chinese:', ord_chinese, ' | chr_123:', chr_123, ' | chr_27387:', chr_27387)

# 字符的整数编码
s = '\u4e2d\u6587'
print(r'\u4e2d\u6587==>', s)

# bytes类型数据
print('b=>', b'ABC', ' || ascii=>', 'ABC'.encode('ascii'), ' || utf-8=>', '中文'.encode('utf-8'))

# -字符串格式化
print('d-%d, f-%f, s-%s, x-%x' % (33, 0.987, 'hello world', 0xf))
print('name-{0}, age-{1:.2f}'.format('xiaoming', 3.14159))
