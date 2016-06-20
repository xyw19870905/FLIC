filename = 'wangjin_01.inp'

f = open(filename, 'r')
lines = f.readlines()
f.close()

npoint = int(lines[0].strip().split(' ')[-1][:-1])

data = []
name = []
for i,v in enumerate(lines):
    if '(' not in v and ')' not in v:
        data.append(v.strip())
    
    if '(' in v and ')' not in v:
        name.append(v.strip().split('(')[-1])
        
ncolumn = len(name)

f = open(filename.split('.')[0]+'.csv', 'w')

for i,v in enumerate(name):
    f.write('%s,' % v)
f.write('\n')

for i in range(npoint):
    for i1 in range(ncolumn):
        f.write('%s,' % data[i+i1*npoint])
        
    f.write('\n')
    
f.close()