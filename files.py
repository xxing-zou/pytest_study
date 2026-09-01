# data={   #python数据类型
#     '数字':[1,1.2],
#     '字符串':['1','1222'],
#     '布尔值':[True,False],
#     '空值':[None],
#     '列表':[[1,2,3],[4,5,6]],
#     '字典':[{'a':1},{'b':2}],
# }
#
# import yaml
# f =open('data.yaml',"w",encoding="utf-8")
# #序列化，允许使用unicode，不对key进行排序
# yaml.safe_dump(data,f,allow_unicode=True,sort_keys=False)
import pprint

import yaml
f =open('data.yaml',"r",encoding="utf-8")
#反序列化，转为pthon变量
data=yaml.safe_load(f)
pprint.pprint(data)#字典