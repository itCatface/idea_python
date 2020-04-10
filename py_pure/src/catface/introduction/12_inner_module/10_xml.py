# -xml[dom&sax&parser]
# sax[start_element&char_data&end_element]
from pyexpat import ParserCreate


class Sax(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def char_data(self, txt):
        print('sax:char_data: %s' % txt)

    def end_element(self, name):
        print('sax:end_element: %s' % name)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

sax = Sax()
parser = ParserCreate()
parser.StartElementHandler = sax.start_element
parser.CharacterDataHandler = sax.char_data
parser.EndElementHandler = sax.end_element
parser.Parse(xml)
