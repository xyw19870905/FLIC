filename = input("FLIC Profile Name: ")

f = open(filename.strip(), 'r')
lines = f.readlines()
f.close()

name = lines[0].strip().split(',')
data = []

for i,v in enumerate(lines[1:]):
    tmp = v.strip().split(',')
    data.extend(tmp)
    
f = open(filename.split('.')[0]+'_re.prof', 'w')

npoint = int(len(data)/len(name))
nname = len(name)

f.write('((bed-top point %d)\n' % npoint)
for i in range(nname):
    f.write('(%s\n' % name[i])
    for j in range(npoint):
        f.write('%s\n' % data[j*nname+i])
    f.write(')\n')    
f.write(')')
f.close()    