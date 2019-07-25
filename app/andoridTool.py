import os
import re


#获取手机可用RAM
def getRAM():
    lines = os.popen("adb shell cat proc/meminfo").readlines() #逐行读取
    name = "MemTotal"
    for line in lines:
        if re.findall(name,line):
            cuplist = line.split(" ")
            while '' in cuplist:       # 将list中的空元素删除
                cuplist.remove('')
            return cuplist[1]

#获取android版本
def getAndroidVersion():
    lines = os.popen("adb shell getprop ro.build.version.release").readlines() #逐行读取
    return lines[0]

#获取手机型号
def getModel():
    lines = os.popen("adb shell getprop ro.product.model").readlines() #逐行读取
    return lines[0]

#获取应用占用Pss
def getTotalPss(packageName):
    """
    packageName:App的包名
    """
    lines = os.popen("adb shell dumpsys meminfo "+packageName).readlines() #逐行读取
    total = "TOTAL"
    for line in lines:
        if re.findall(total, line): # 找到TOTAL 这一行
            lis = line.split(" ")  #将这一行，按空格分割成一个list
            while '' in lis:       # 将list中的空元素删除
                lis.remove('')
            return lis[1] #返回总共内存使

#获取应用占用VSS和Rss
def getVssAndRss(packageName):
    """
    packageName:App的包名
    """
    li = os.popen("adb shell top -m 100 -n 1 -s cpu").readlines()
    name = packageName
    for line in li:
        if re.findall(name,line):
            cuplist = line.split(" ")
            if cuplist[-1].strip() == packageName:
                while '' in cuplist:       # 将list中的空元素删除
                    cuplist.remove('')
                return cuplist[5],cuplist[6]

#获取应用占用CPU
def getCpu(packageName):
    """
    packageName:App的包名
    """
    li = os.popen("adb shell top -m 100 -n 1 -s cpu").readlines()
    name = packageName
    for line in li:
        if re.findall(name,line):
            cuplist = line.split(" ")
            if cuplist[-1].strip() == packageName:
                while '' in cuplist:       # 将list中的空元素删除
                    cuplist.remove('')
                return cuplist[2]

