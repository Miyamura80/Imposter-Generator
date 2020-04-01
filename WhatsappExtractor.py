import re

mainFile = "WhatsApp Chat with Crap in a Wrap.txt"

with open("WhatsApp_Chat_with_Chua_Hou.txt", "r", encoding='utf8') as textFile:
    wholeChat = textFile.read()

export = open("ChuaHou.txt", "w", encoding='utf8')

result = re.findall('Chua Hou: (.*)\n', wholeChat)
count = 0
for text in result:
    if not (re.match('<', text) or re.match('http', text)):
        count += 1
        export.write(text)
        export.write('\n')

export.close()
