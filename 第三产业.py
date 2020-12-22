import matplotlib.pyplot as plt
with open('中美服务业增加值.txt','r',encoding='utf-8') as f:
    f1=f.readlines()
with open('中美服务业增加值占GDP比重','r',encoding='utf-8') as f:
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

years1=[]
years2=[]
China_GDP1=[]
China_per1=[]
America_GDP1=[]
America_per1=[]

for line in f1:
    a=line.split('\t')
    years1.append(int(a[0]))
    China_GDP1.append(abstract_gdp(a[1]))
    America_GDP1.append(abstract_gdp(a[2]))

for line in f2:
    b=line.split('\t')
    years2.append(int(b[0]))
    China_per1.append(abstract_percent(b[1]))
    America_per1.append(abstract_percent(b[2]))

plt.rcParams['font.family']='SimHei'
plt.subplot(1,2,1)
plt.plot(years1,China_GDP1,label="中国第三产业GDP总量")
plt.plot(years1,America_GDP1,label="美国第三产业GDP总量")
plt.title("中美第三产业GDP总量对比")
plt.legend()

plt.subplot(1,2,2)
plt.plot(years2,China_per1,label="中国第三产业占GDP比")
plt.plot(years2,America_per1,label="美国第三产业占GDP比")
plt.title("中美第三产业GDP占比对比")
plt.legend()

plt.savefig('中美第三产业对比')