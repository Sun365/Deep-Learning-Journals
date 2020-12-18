import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
from pandas.plotting import scatter_matrix
import urllib.request
# from celluloid import Camera #自动录制，待研究

SEED=1234
DATA_FILE='tumors.csv'

# Set seed for reproducibility
np.random.seed(SEED)

# Load data from GitHub to this notebook's local drive
url="https://raw.githubusercontent.com/madewithml/basics/master/data/tumors.csv"
response=urllib.request.urlopen(url)
html=response.read()
print(html[:100])
with open(DATA_FILE,'wb') as fp:
    fp.write(html)
print(fp)

# Raw data
df=pd.read_csv(DATA_FILE,header=0,encoding='gbk')
print(df.head())

# Define X and y
X=df[['leukocyte_count','blood_pressure']].values
y=df['tumor_class'].values

# 过程中间产物抽查 # 此段代码可有可无
print('part1 \n',X[:20,0],'part2 \n',X[:20,1],len(X)) 
print(len(y),y[:20])

# Plot data

plt.ion() #将画图模式改为交互模式

colors = {'benign': 'blue', 'malignant': 'red'} # 数据元素颜色匹配字典

for i in range(len(X)):
    ix=X[:i,0]
    iy=X[:i,1]
    plt.cla()
    fig=plt.scatter(ix, iy,c=[colors[_y] for _y in y[:i]], s=25,edgecolors='k',marker = 'o')
    
    # 创建图例
    first_legend = plt.legend(labels=['Malignant'],loc='upper right')
    ax = plt.gca().add_artist(first_legend)
    dot,=plt.plot([], "ro",markersize=4.5, color='blue')  # 实在搞不定，于是引入了一个图标，但是圆的边缘颜色还没搞定
    plt.legend(handles=[dot],labels=["Benign"],loc='upper left')

    # 图片基本元素设置
    plt.xlim(0,25) # 锁定图片大小，不会随数据增加而变化    
    plt.ylim(10,20)
    plt.title("Tumor Prediction")
    plt.xlabel('Leukocyte count')
    plt.ylabel('Blood pressure')

    plt.pause(0.001) # 闪图，窗口停留时间

    # 取所有图片
    plt.rcParams['savefig.dpi'] = 100 #统一图片像素，不然会导致动图位移
    plt.rcParams['figure.dpi'] = 100 #统一分辨率
    #plt.figure(figsize=(600, 400), dpi=80)
    plt.savefig('learning place\LiaoXF-python\Machine Learning Basics\Data Visualization\Pics\%s.jpg'% i)


    # 以下代码为减少保存数量，间隔存图
    '''
    if i%5==1: # 每五存一
        plt.rcParams['savefig.dpi'] = 100 #统一图片像素
        plt.rcParams['figure.dpi'] = 100 #统一分辨率
        plt.savefig('learning place\LiaoXF-python\Machine Learning Basics\Data Visualization\Pics\%s.jpg'% i)
        # “...\Pics\”，为目录文件夹
        # “%s.jpg'% i”，批量命名
    else:
        pass 
    '''
    

    # 录制
    # camera.snap() #待研究

plt.ioff()
plt.show() #显示最后一张图，此代码可有可无

