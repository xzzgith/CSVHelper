# coding=utf-8

import re

with open('Localizable.strings','r+') as f:
    str = f.read()
    pattern = re.compile(r'= \".*\"*')
    result1 = pattern.findall(str)
    print("count = %d",len(result1))
    for t in result1:
        tmpList = t.split('= ')
        tmpStr = tmpList[1]
        tmpStr = tmpStr[1:]
        tmpStr = tmpStr[:-2]
        print tmpStr



