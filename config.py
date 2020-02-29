'''
城市迁徙排名数据只能一个城市一爬，需要给出城市的code
单次任务只能抓取迁入或者迁出数据选其一
中国所有省市级行政区划代码在文件ChinaAreaCode.csv中
依赖库: requests、json、time、csv
'''

# 指定抓取任务的抓取数据类型'move_in'or'move_out'即抓取迁入还是迁出数据
task_type = 'move_in'
# 要抓取的时间列表
time_list = [str(t) for t in range(20200101, 20200132)] + [str(t) for t in range(20200201, 20200229)]
# 城市迁徙排名数据保存路径
paiming_path = '/Users/yych97/data/baidu_qx/上海市迁入数据/'
# 全国各城市迁徙指数数据保存路径
zhishu_path = '/Users/yych97/data/baidu_qx/各城市迁入指数/'
# 是否抓取迁徙排名数据
paiming = False
# 是否抓取全国各城市指数数据
zhishu = True
# 城市迁徙排名数据要抓取的城市citycode
paiming_citycode = '310000'