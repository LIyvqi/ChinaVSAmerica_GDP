import matplotlib.pyplot as plt
with open('GDP年增长率','r',encoding='utf-8') as f:
    lines=f.readlines()
years=[]
China=[]
America=[]
for line in lines[1:]:
    a=line.split('\t')
    years.append(int(a[0]))
    China.append(float(a[1].split('%')[0]))
    America.append(float(a[2].split('%')[0]))

plt.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False

plt.plot(years,China,label="中国GDP增速")
plt.plot(years,America,label="美国GDP增速")
plt.title("中美GDP增速对比")
plt.legend()
plt.savefig('中美GDP增速对比')