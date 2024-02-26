import re

f = open("C:\\Users\\joaop\\Documents\\Uni\\Y3-S2\\PL\\PL2024\\TPC3\\input.txt", "r")
c = 0
switch = False
nums = []
fullStr = ""
for l in f:
    if re.search(r"on", l) or switch:
        if re.search(r"on", l) and not switch:
            mix = re.split(r"on", l)[1]
            switch = True
        else:
            mix = l

        if re.search(r"off", mix):
            line = re.split(r"off", mix)[0]
            switch = False
        else:
            line = mix

        fullStr += line
    else:
        print("No on found")

splitBySpace = re.split(r"=", fullStr)
for part in splitBySpace:
    # print(part)
    lis = re.findall(r"[+-]?\d+", part)
    for no in lis:
        c += int(no)
    print(c)
