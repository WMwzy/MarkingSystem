import tkinter as tk
import ttkbootstrap as ttk
from datetime import datetime
from data_operation import get_yaml_data,dump_data_to_yaml
from tkinter.messagebox import *
from score import caculate_score

data = {}

def upload_data():
    dic = {}
    dic["time"] = str(time.get())
    dic["amount"] = int(amount.get())
    data[str(cbox.get())] = dic
    cbox.set("")
    con1.set("")
    con2.set("")
    showinfo("提示","上传成功！")

def caculate():
    global data,stuList
    data,stuList,result = caculate_score(data,stuList)
    lowest_score = 100
    for key,value in result.items():
        if value < lowest_score:
            lowest_score = value
    record_score(data,stuList)
    showinfo("提示","计算完成！最低分为"+str(lowest_score))
    # showinfo("提示","计算完成！")

def record_score(data,stuList):
    file_data = {}
    file_data["caculate_time"] = datetime.now()
    file_data["data"] = data
    dump_data_to_yaml(file_data,"score.yaml","a")
    dump_data_to_yaml(stuList,"stuList.yaml","w")

root_window = ttk.Window(themename="pulse")
root_window.title('评分系统')
# 设置窗口大小变量
width = 300
height = 230
screenwidth = root_window.winfo_screenwidth()
screenheight = root_window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root_window.geometry(size_geo)
root_window.resizable(False,False)

ttk.Label(root_window,text="学生姓名").place(x=20,y=25)
cbox = ttk.Combobox(root_window,width=16)
cbox.place(x=100,y=20)
# 获取combobox值
stuList = get_yaml_data("stuList.yaml")
temp = []
for i in stuList:
    temp.extend(i.keys())
cbox['value'] = tuple(temp)

ttk.Label(root_window,text="上传时间").place(x=20,y=75)
con1 = ttk.StringVar()
time = tk.Entry(root_window,width=19,textvariable=con1)
time.place(x=100,y=75)

ttk.Label(root_window,text="单词数量").place(x=20,y=120)
con2 = ttk.StringVar()
amount = tk.Entry(root_window,width=19,textvariable=con2)
amount.place(x=100,y=120)

btn = ttk.Button(root_window,text="上传",width=6,command=upload_data)
btn.place(x=60,y=170)

btn = ttk.Button(root_window,text="计算",width=6,command=caculate)
btn.place(x=160,y=170)

root_window.mainloop()
