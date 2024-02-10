import sys

f = open("C:\\Users\\joaop\\Documents\\Uni\\Y3-S2\\PL\\TPC1\\emd.csv", "r")
h = f.readline()
h = h.split()

pplC: int = 0
ablePPl: int = 0
sports = []
age04: list[float] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
age59: list[float] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for l in f:
    s = l.split(',')
    pplC += 1
    if s[12].lower() == "true\n":
        ablePPl += 1

    if s[8] not in sports:
        sports.append(s[8])

    if int(s[5]) % 10 < 5:
        age04[int(s[5]) // 10] += 1
    else:
        age59[int(s[5]) // 10] += 1

# Treat the values
i = 0
while i < len(age04):
    age04[i] = age04[i] * 100 / pplC
    age59[i] = age59[i] * 100 / pplC
    i+=1

ablePPl = ablePPl * 100 // pplC

sports.sort()

i=0
while i < len(age59):
    if age04[i] > 0:
        print(str(i) + '0-' + str(i) + '4' + str(age04[i]) + '%')
    if age59[i] > 0:
        print(str(i) + '5-' + str(i) + '9: ' + str(age59[i]) + '%')
    i += 1

print(str(ablePPl) + '%')
print(sports)
