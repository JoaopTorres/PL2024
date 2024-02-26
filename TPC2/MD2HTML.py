import sys
import re

f = open("C:\\Users\\joaop\\Documents\\Uni\\Y3-S2\\PL\\PL2024\\TPC2\\out.txt", "w")
i = open("C:\\Users\\joaop\\Documents\\Uni\\Y3-S2\\PL\\PL2024\\TPC2\\examples.txt", "r")

for l in i:
    l = re.sub(r"[*]{2}(.*)[*]{2}", r"<b>\1</b>", l)
    l = re.sub(r"[*]{1}(.*)[*]{1}", r"<i>\1</i>", l)

    l = re.sub(r"[#]{3}(.*)", r"<h3>\1</h3>", l)
    l = re.sub(r"[#]{2}(.*)", r"<h2>\1</h2>", l)
    l = re.sub(r"[#]{1}(.*)", r"<h1>\1</h1>", l)

    l = re.sub(r'[!][\[](.*?)[\]?][\(](.*?)[\)]', r'<img src="\2" alt="\1">', l)
    l = re.sub(r'[\[](.*?)[\]][\(](.*?)[\)]', r'<a href="\2">\1</a>', l)

    l = re.sub(r'[0123456789]*[.][ ](.*)', r"<ol> <li>\1</li> </ol>", l)

    f.write(l)
