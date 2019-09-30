#coding=utf-8
f0 = open("t0.txt", "w")
f1 = open("t1.txt", "w")
f2 = open("t2.txt", "w")

with open('csv12.csv','r+') as f:
    for s in f.readlines():
        list = s.split(',')
        for i,j in enumerate(list):
            j = j.replace('\n','')
            j = j.replace('\r','')
            if i==0:    
                f0.write('"' + j + '"')
                f1.write('"' + j + '"')
                f2.write('"' + j + '"')
            elif i==1:
                f0.write(' = ' + '"' + j + '";\n')
            elif i==2:
                f1.write(' = ' + '"' + j + '";\n')
            else:
                f2.write(' = ' + '"' + j + '";\n')

f0.close()
f1.close()
f2.close()


    

