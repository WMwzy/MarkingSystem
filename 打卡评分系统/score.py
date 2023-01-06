import numpy as np
import datetime
import time
import sys

def caculate_score(data,stuList):
    result = {}
    weight = get_weight()
    
    max_amount = 0
    min_amount = 9999
    max_time = 0
    min_time = 999999
    for _,value in data.items():
        time_len = cal_time(value["time"])
        amount = value["amount"]
        if time_len > max_time:
            max_time = time_len
        if time_len < min_time:
            min_time = time_len
        if amount > max_amount:
            max_amount = amount
        if amount < min_amount:
            min_amount = amount
    
    today = datetime.date.today()
    today = today.strftime("%Y-%m-%d")
    max_day = 0
    min_day = 99999
    for i in stuList:
        stu = list(i.keys())[0]
        if stu not in data:
            i[stu]["is_continuous"] = False
            i[stu]["days"] = 0
            continue
        if abs(differ(today,i[stu]["last_day"])) == 1:
            i[stu]["is_continuous"] = True
            i[stu]["days"] += 1
        elif differ(today,i[stu]["last_day"]) == 0:
            # print("今日已计算过！")
            sys.exit(0)
        else:
            i[stu]["is_continuous"] = False
            i[stu]["days"] = 1
        i[stu]["last_day"] = today
        if i[stu]["days"] > max_day:
            max_day = int(i[stu]["days"])
        if i[stu]["days"] < min_day:
            min_day = int(i[stu]["days"])

    score = {}
    for key,value in data.items():
        dic = {}
        dic["amount_score"] = (int(value["amount"]) - min_amount) / (max_amount - min_amount)
        dic["time_score"] = (max_time - cal_time(value["time"])) / (max_time - min_time)
        for i in stuList:
            if list(i.keys())[0] == key:
                dic["days_score"] = (i[key]["days"] - min_day) / (max_day - min_day)
        score[key] = dic
        result[key] = dic["amount_score"]*weight[0] + dic["time_score"]*weight[1] + dic["days_score"]*weight[2]
        data[key]["score"] = result[key]
    
    data["weight"] = weight
    return data,stuList,result

def get_weight():
    weight = []
    lis = list(np.random.normal(loc=0.0,scale=0.1,size=3))
    for i in range(len(lis)):
        weight.append(float(lis[i]))
    all = 0
    for i in range(len(weight)):
        weight[i] = abs(weight[i])
        all += weight[i]
    for i in range(len(weight)):
        weight[i] = weight[i]/all
    return weight

def cal_time(str):
    time = str.split(":")
    time_len = int(time[0])*60 + int(time[1])
    return time_len

def differ(day1,day2):
    t1 = int(time.mktime(time.strptime(day1,"%Y-%m-%d")))
    t2 = int(time.mktime(time.strptime(day2,"%Y-%m-%d")))
    differ = (datetime.datetime.fromtimestamp(t2)-datetime.datetime.fromtimestamp(t1)).days
    return differ