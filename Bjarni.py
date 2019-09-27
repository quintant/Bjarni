import collections
file = open("laxdaela_saga.en.txt", "r+")
s = file.read().lower()
tr = s.split(' ')
aa = {}
for i in range(len(tr)):
    if '.' in tr[i]:
        tr[i] = tr[i].replace('.', '')
    fret = ""
    for u in tr[i]:
        if u.isalnum():
            fret += u
    if fret in aa:
        aa[fret] += 1
    else:
        aa[fret] = 1

aa = sorted(aa.items(), key=lambda kv: kv[1], reverse=True)
aa = collections.OrderedDict(aa)
#print(" --- most frequent words --- ")
lel = 1
out = open("tidni.txt", "w+")
out.write(" --- most frequent words --- " + '\n')
for io in aa:
    out.write(str(lel) + "   " + str(io) + "          " + str(aa[io])+ '\n')
    #print(str(lel) + "   " + str(io) + "          " + str(aa[io]))


