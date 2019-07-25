import datetime
import time
import threading
import andoridTool 
import csv
import os
import asyncio
#获取时间
def getNowTime():
    #time=datetime.datetime.now().strftime(r'%Y%m%d%H%M%S')
    time=datetime.datetime.now().strftime(r'%Y%m%d')
    return(time)

#获取时间
def getNowDate():
    time=datetime.datetime.now().strftime(r'%Y/%m/%d %H:%M:%S')
    return(time)

#数据保存到csv文件中
def setDataCSV(lists):
    fileName=r".data"+str(getNowTime())+r".csv"
    if os.path.exists(fileName):
        with open(fileName,mode='a',newline='') as datacsv:
            csvwriter = csv.writer(datacsv,dialect = ("excel"))
            csvwriter.writerow(lists)
    else:
        lists=['time','cpu','PSS','VSS','RSS']
        with open(fileName,mode='a',newline='') as datacsv:
            csvwriter = csv.writer(datacsv,dialect = ("excel"))
            csvwriter.writerow(lists)
        


#运行程序
def run(frequency,packageName):
    '''
    frequency：刷新平次，秒
    packageName：应用包名
    '''
    # Model=andoridTool.getModel()
    # print(Model)
    # AndroidVersio=andoridTool.getAndroidVersion()
    # print(AndroidVersio)
    # RAM=andoridTool.getRAM()
    # print(RAM)
    cpu=andoridTool.getCpu(packageName)
    
    TotalPss=andoridTool.getTotalPss(packageName)
    
    VssAndRss=andoridTool.getVssAndRss(packageName)
    
    if(cpu==None):
        cpu==0

    if(TotalPss==None):
        TotalPss==0

    if(VssAndRss==None):
        VssAndRss==0

    lists=[str(getNowDate()),str(cpu),str(TotalPss),str(VssAndRss[0]),str(VssAndRss[1])]
    print(lists)
    setDataCSV(lists)
    
    



