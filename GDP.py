import matplotlib.pyplot as plt
def abstract_gdp(L):
    a = L.split('亿')
    if '万' in a[0]:
        s = float(a[0][:-1]) * 10000
    else:
        s = float(a[0])
    return s

def abstract_percent(L):
    return float(L.split('%')[0])

with open('GDP.txt', 'r',encoding='utf-8') as f:
    lines=f.readlines()
China_GDP=[]
America_GDP=[]
China_percent=[]
America_percent=[]
years=[]
for line in lines[2:]:
    a=line.split('\t')
    years.append(int(a[0]))
    China_GDP.append(abstract_gdp(a[1]))
    China_percent.append(abstract_percent(a[2]))
    America_GDP.append(abstract_gdp(a[3]))
    America_percent.append(abstract_percent(a[4]))


plt.rcParams['font.family']='SimHei'
plt.subplot(1,2,1)
plt.plot(years,China_GDP,label="中国GDP总量")
plt.plot(years,America_GDP,label="美国GDP总量")
plt.title("中美GDP总量对比")
plt.legend()

plt.subplot(1,2,2)
plt.plot(years,China_percent,label="中国GDP占全球比")
plt.plot(years,America_percent,label="美国GDP占全球比")
plt.title("中美GDP占全球百分比对比")
plt.legend()

plt.savefig('中美GDP对比')
