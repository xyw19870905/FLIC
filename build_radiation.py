import math
import os

eps = 1.0e-8
bed_length = 10.5    # 炉排真实长度
hor_length = 10.5    # 炉排水平长度
angle = math.acos(hor_length/bed_length)

def get_data(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    
    x = []
    t = []
    for i,v in enumerate(lines):
        x.append(float(v.strip().split('\t')[0]))
        t.append(float(v.strip().split('\t')[1]))
        
    return x, t

def rebuild_temperature(x, t):
    tmp1 = []
    for i,v in enumerate(x):
        if v not in tmp1:
            tmp1.append(v)
    tmp1.sort()
    print(tmp1)
    
    npoints = []
    tmp2 = []
    for i,v in enumerate(tmp1):
        npoints.append(0)
        tmp2.append(0.0)
            
    for i,v in enumerate(x):
        for i1, v1 in enumerate(tmp1):
            if v1 == v:
                npoints[i1] += 1
                tmp2[i1] += float(t[i])
    
    print((len(tmp1)-1)/14.0, round((len(tmp1)-1)/14.0))
    gap = int(input('Input gap: '))
    
    dl = []
    dt = []
    for i,v in enumerate(tmp1[::gap]):
        if i < len(tmp1[::gap])-1:
            dl.append(float(tmp1[(i+1)*gap])-float(v))
            tt1 = 0.0
            tt2 = 0
            for i1 in range(gap):
                tt1 += tmp2[i*gap+i1]
                tt2 += npoints[i*gap+i1]
            dt.append(tt1/tt2)
        else:
            dl.append(float(tmp1[-1])-float(v))
            tt1 = 0.0
            tt2 = 0
            for i1 in range(len(tmp1)-i*gap-1):
                tt1 += tmp2[i*gap+i1]
                tt2 += npoints[i*gap+i1]
            dt.append(tt1/(tt2+eps))

    print('Number of delta L is ', len(dl))
    return dl, dt
    
def write_flic_file(dl, dt):
    f = open('to_flic.txt', 'w')
    f.write('over-bed radiation temperature profile\n')
    f.write('emissivity:\n1.000000\n')
    f.write('number of points:\n%d\n' % len(dl))
    f.write('length span profile (m)\n')
    for i,v in enumerate(dl):
        f.write('%f\n' % (v/math.cos(angle)))
    f.write('radiative temperature (k)\n')
    coeff = float(input('Input temperature coeff: '))
    for i,v in enumerate(dt):
        f.write('%f\n' % (v*coeff))
    f.write('end of file')
    f.close()

def rewrite_fluent_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    
    x = []
    t = []
    for i,v in enumerate(lines[4:-1]):
        x.append(float(v.strip().split('\t')[0]))
        t.append(float(v.strip().split('\t')[1]))
        
    f = open('tmp', 'w')
    for i,v in enumerate(x):
        f.write('%.6f\t%.6f\n' % (v, t[i]))
    f.close()
   
def main():
    filename = input('Input Fluent Radiation File Name: ')
    rewrite_fluent_file(filename)
    x, t = get_data('tmp')
    dl, dt = rebuild_temperature(x, t)
    write_flic_file(dl, dt)
    os.system('del tmp')

    
if __name__ == '__main__':
    main()