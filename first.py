import csv
import pandas as pd
import redis , json
import requests
import zipfile
import os, re
from ast import literal_eval
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Bhav:
    def __init__(self):
        try:
            #connecting to redis database
            self.r = redis.StrictRedis(host="localhost",port=6379,password='',charset="utf-8", decode_responses=True)
        except:
            print ("database not connected")
    
    def downloadExtract(self):

        #download the file
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : "/nagnara2/Documents"}
        chromeOptions.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome()
        driver.get("https://www.bseindia.com/markets/equity/EQReports/BhavCopyDebt.aspx?expandable=3")
        time.sleep(10)
        frame1 = driver.find_element_by_xpath('//*[@id="wrap"]/div/div[3]/div[2]/div/div[2]/div/div/table/tbody/tr/td/iframe')
        driver.switch_to_frame(frame1)
        elem = driver.find_element_by_xpath('//*[@id="btnhylZip"]')
        elem.send_keys(Keys.RETURN)
        time.sleep(10)
        driver.close()
        
        #open and extract the file
        open('bhav.zip', 'wb').write(r.content)
        correct_csv = zipfile.ZipFile('bhav.zip','r')
        correct_csv.extractall("./")

        #rename the file
        for i in os.listdir('.'):
            if re.match('EQ',i):
                os.rename(i,"bhav.csv")

    def readCSV(self):
        filename = "bhav.csv"
        self.df = pd.read_csv(filename,header=0)

    def storeInRedis(self):

    #clear all the keys in the DataBase before adding.
        for key in self.r.scan_iter():
            self.r.delete(key)

        #adding the values in the database
        for i in range(len(self.df)):
            list = self.df.iloc[i]
            self.r.hmset(list[1],{'SC_NAME':list[1],'SC_CODE':list[0],"OPEN":list[4],
            "HIGH":list[5],"LOW":list[6],"CLOSE":list[7]})   

    def printValues(self,name=None):
        lis = {}
        if name == None:
            for key in self.r.scan_iter():
                lis[key]=(self.r.hgetall(key))
            json_str = json.dumps(lis)
            lis = json.loads(json_str)
            return lis 
        else:
            str = "*"+name+"*"
            list1 = {}
            for key in self.r.scan_iter(str):
                list1[key]=(self.r.hgetall(key))
            jsonstr = json.dumps(list1)
            list1=json.loads(jsonstr)
            return list1
           
