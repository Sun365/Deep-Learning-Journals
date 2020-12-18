import os
import re
import imageio
path=r'C:\Users\suntw\anaconda3\envs\pytorch\learning place\LiaoXF-python\Machine Learning Basics\Data Visualization\Pics'

# 本段要解决的是 图片的排序问题
list = next(os.walk(path))[2]
print('排序前：无序 Out of order',list[:20])

list.sort(key=lambda x: int(x.split('.jpg')[0])) # 丢弃'.jpg'字段，将图片名称变成整数（int)，排序
print('排序后：有序 Ordered',list[:20])

filenames=[]
for files in list:    
    if files.endswith('jpg') or files.endswith('jpeg') or files.endswith('png'):
    	file=os.path.join(path,files)
    	filenames.append(file)

images=[]
for filename in filenames:
	images.append(imageio.imread(filename))
imageio.mimsave('my.gif',images,duration=0.1) # "duration=0.1"，每张图片的出现时间

'''参考 reference'''
# https://blog.csdn.net/weixin_43568160/article/details/85680497
# https://blog.csdn.net/v1_vivian/article/details/74980074
# python下使用sort()函数对目录下文件名进行多条件排序
# https://blog.csdn.net/Kobaayyy/article/details/105132639