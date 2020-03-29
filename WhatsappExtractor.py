import re

with open("WhatsApp Chat with Crap in a Wrap.txt", "r", encoding='utf8') as textFile:
    wholeChat = textFile.read()

export = open("MichaelTexts.txt", "w", encoding='utf8')

result = re.findall('Michael: (.*)\n', wholeChat)
count = 0
for text in result:
    if not (re.match('<', text) or re.match('http', text)):
        count += 1
        export.write(text)
        export.write('\n')

export.close()
