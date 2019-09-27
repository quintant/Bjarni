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

aa = sorted(aa.items(), key=lambda kv: kv[1])
aa = collections.OrderedDict(aa)
for io in aa:
    print(str(io) + "____" + str(aa[io]))


