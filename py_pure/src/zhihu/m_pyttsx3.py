# install ==> sudo apt-get install pyttsx3
# OSError libespeak.so.1 error: no such file or directory ==> sudo apt-get install espeak
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pyttsx3
engine = pyttsx3.init()
engine.say("hello world")
voices = engine.getProperty('voices')
for v in voices:
    print('v:', v)

print('voices:', voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('voice', 'zh')
voice = engine.getProperty('voice')
print('voice:', voice)
engine.runAndWait()


# with open("./../imooc/spider_four_famous_novels_180524/temp_file_2/《金瓶梅》目录.txt",'r',encoding='utf-8') as f:
#     while 1:
#         line = f.readline()
#         print(line, end = '')
#         engine.say(line)
#         engine.runAndWait()
#
# import struct
#
# v = struct.calcsize("P")
# print(v)


# from comtypes.client import CreateObject
# engine = CreateObject("SAPI.SpVoice")
# stream = CreateObject("SAPI.SpFileStream")