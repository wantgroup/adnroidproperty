import threading 
import time
import runTool 

packageName="com.tencent.mm"
frequency='5'
# 定时器
def fun_timer():

    runTool.run(frequency,packageName)

    global timer
    timer = threading.Timer(5, fun_timer)
    timer.start()

timer = threading.Timer(1, fun_timer)
timer.start()