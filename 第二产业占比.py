import matplotlib.pyplot as plt
with open('中美工业增加值占比','r',encoding='utf-8') as f:
    f2=f.readlines()

def abstract_gdp(L):
    a = L.split('亿')
    if '万' in a[0]:
        s = float(a[0][:-1]) * 10000
    else:
        s = float(a[0])
    return s

def abstract_percent(L):
    return float(L.split('%')[0])

years2=[]
China_per2=[]
America_per2=[]

for line in f2:
    b=line.split('\t')
    years2.append(int(b[0]))
    China_per2.append(abstract_percent(b[1]))
    America_per2.append(abstract_percent(b[2]))

plt.rcParams['font.family']='SimHei'

plt.plot(years2,China_per2,label="中国第二产业占GDP比")
plt.plot(years2,America_per2,label="美国第二产业占GDP比")
plt.title("中美工业增加值占GDP比重对比")
plt.legend()

plt.savefig('中美工业增加值占GDP比重对比')