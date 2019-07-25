#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import runTool
csvwriter =None
def setDataCSV(lists):
    fileName=r".\data\\"+str(runTool.getNowTime())+r".csv"
    with open(fileName,mode='a',newline='') as datacsv:
        csvwriter = csv.writer(datacsv,dialect = ("excel"))
    csvwriter.writerow(lists)

