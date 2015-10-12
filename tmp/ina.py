import sys

f = open(sys.argv[1])

lines = f.readlines()
lines = [x.strip() for x in lines]

d1 = list()
d2 = list()

for line in lines:
    print line
    p,n = line.split('*')
    n = n[:-1].strip()
    p = p.strip()
    d1.append("%s  *truthTreeBd_%s;" % (p, n))
    d2.append("truthTreeBd->SetBranchAddress(\"%s\",&truthTreeBd_%s);" % (n,n))

d = open(sys.argv[1]+'-dest','w')
d.writelines('\n'.join(d1))
d.write('\n')
d.writelines('\n'.join(d2))
d.close()
f.close()