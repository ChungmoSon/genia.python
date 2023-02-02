import re

filedata =''
with open("EN.txt", 'r', encoding='utf-8') as fp:
    for i in fp:
        a=fp.readline()
        if ';' in a:
            filedata+=a.replace(';','\n'+a.split(' ')[0])
        else:
            filedata+=a
with open('new_EN.txt', 'w', encoding='utf-8') as fp2:
    fp2.write(re.sub("{|}|\||_","",filedata))
