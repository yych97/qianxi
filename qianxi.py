import requests
import json
import time
import csv
from config import time_list, paiming_path, zhishu_path, paiming, zhishu, paiming_citycode, task_type

# now = time.strftime('%Y-%m-%d-%H-%M-%S')

# for t in time_list:
#     print(t)

def get_city_moveinout():
    '''
    获取指定城市迁徙规模排名数据
    '''
    for t in time_list:
        url = 'https://huiyan.baidu.com/migration/cityrank.json?dt=city&id={}&type={}&date={}'.format(paiming_citycode, task_type, t)
        data = json.loads(requests.get(url).text)['data']
        header = data['list'][0].keys()
        with open(paiming_path + '{}_{}_{}.csv'.format(paiming_citycode, task_type, t), "w+", newline="") as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow(header)
            for city in data['list']:
                row = [city[h] for h in header]
                writer.writerow(row)
        print(t + ' OK')

def get_city_migrationIndex():
    file = csv.reader(open('ChinaAreaCode.csv', 'r'))
    for row in file:
        if row[0] != 'code':
            code = row[0]
            name = row[1]
            try:
                url = 'https://huiyan.baidu.com/migration/historycurve.json?dt=city&id={}&type={}'.format(code, task_type)
                text = json.loads(requests.get(url).text)
                data = text['data']['list']
                keys = data.keys()
                header = ['date', 'index']
                with open(zhishu_path + '{}_{}_{}.csv'.format(code, name, task_type), "w+", newline="") as csv_file:
                    writer=csv.writer(csv_file)
                    writer.writerow(header)
                    for day in data.keys():
                        row = [day, data[day]]
                        writer.writerow(row)
                print(code + ' OK')
            except:
                print(code + ' No Data')

def main():
    if paiming == True:
        get_city_moveinout()
    if zhishu == True:
        get_city_migrationIndex()

    
if __name__ == '__main__':
    main()